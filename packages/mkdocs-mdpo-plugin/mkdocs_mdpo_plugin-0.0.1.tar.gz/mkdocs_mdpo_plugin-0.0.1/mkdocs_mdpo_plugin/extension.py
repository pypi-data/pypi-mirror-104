import polib
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

from mkdocs_mdpo_plugin.plugin import MkdocsBuild


class MkdocsMdpoTreeProcessor(Treeprocessor):
    def run(self, root):
        mdpo_plugin = MkdocsBuild().mdpo_plugin
        current_build_extensions = (
            mdpo_plugin.mkdocs_build_config['markdown_extensions']
        )
        current_page = mdpo_plugin.current_page
        if not hasattr(current_page, '_language'):
            return

        po = current_page._po

        current_page._po_msgids = []
        current_page._po_msgstrs = []
        current_page._disabled_msgids = []
        for entry in po:
            current_page._po_msgids.append(polib.unescape(entry.msgid))
            current_page._po_msgstrs.append(polib.unescape(entry.msgstr))
        for entry in current_page._po_disabled_entries:
            current_page._disabled_msgids.append(polib.unescape(entry.msgid))

        def process_translation(node, msgid):
            if msgid not in current_page._po_msgstrs:
                if msgid in current_page._po_msgids:
                    for entry in po:
                        if entry.msgid == msgid:
                            if entry.msgstr:
                                node.text = entry.msgstr
                            entry.obsolete = False
                elif msgid not in current_page._disabled_msgids and \
                        msgid not in mdpo_plugin._msgids_to_ignore:
                    current_page._po_msgids.append(msgid)
                    po.append(
                        polib.POEntry(msgid=msgid, msgstr=''),
                    )

        def node_should_be_processed(node):
            if 'pymdownx.tasklist' in current_build_extensions and \
                    node.tag in ['li', 'p'] and len(node.text) > 2 and \
                    node.text[:3] in ['[ ]', '[x]', '[X]']:
                return False
            return True

        def iterate_childs(_root):
            for child in _root:
                # print(child.tag, child.text, child.attrib)
                if child.text and not child.text[1:].startswith('wzxhzdk:'):
                    if not node_should_be_processed(child):
                        continue
                    process_translation(
                        child,
                        ' '.join(child.text.split('\n')),
                    )
                iterate_childs(child)

        iterate_childs(root)
        po.save(current_page._po_filepath)

        MkdocsBuild().mdpo_plugin.current_page = current_page


class MkdocsMdpoTitlesTreeProcessor(Treeprocessor):
    def run(self, root):
        mdpo_plugin = MkdocsBuild().mdpo_plugin
        current_build_extensions = (
            mdpo_plugin.mkdocs_build_config['markdown_extensions']
        )
        current_page = mdpo_plugin.current_page
        if not hasattr(current_page, '_language'):
            return

        po = current_page._po

        def process_translation(node, msgid):
            if msgid not in current_page._po_msgstrs:
                if msgid in current_page._po_msgids:
                    for entry in po:
                        if entry.msgid == msgid:
                            if entry.msgstr:
                                node.attrib['title'] = entry.msgstr
                            entry.obsolete = False
                elif msgid not in current_page._disabled_msgids and \
                        msgid not in mdpo_plugin._msgids_to_ignore:
                    current_page._po_msgids.append(msgid)
                    po.append(
                        polib.POEntry(msgid=msgid, msgstr=''),
                    )

        def node_should_be_processed(node):
            if node.tag == 'abbr' and 'abbr' in current_build_extensions:
                # abbreviations titles would be duplicated in msgids
                return False
            elif node.get('class') in ['emojione', 'twemoji', 'gemoji'] and \
                    'pymdownx.emoji' in current_build_extensions:
                # don't add ':+1:' or ':heart:' as msgid
                return False
            elif node.get('class') == 'task-list-item' and \
                    'pymdownx.tasklist' in current_build_extensions:
                return False
            return True

        def iterate_childs(_root):
            for child in _root:
                # print("TITLE", child.tag, child.text, child.attrib)

                # TODO: add support for other attribute names translation
                #       globally (any element including that attribute)
                #       and for `attr_list` officialed supported extension
                if 'title' in child.attrib and \
                        'mdpo-notitle' not in child.attrib and \
                        node_should_be_processed(child):
                    process_translation(
                        child,
                        child.attrib['title'],
                    )
                iterate_childs(child)

        iterate_childs(root)
        current_page._po.save(current_page._po_filepath)


class MkdocsMdpoExtension(Extension):
    def extendMarkdown(self, md):
        # run first
        md.treeprocessors.register(
            MkdocsMdpoTreeProcessor(self),
            'mkdocs-mdpo-tree',
            88887,
        )

        # run latest
        md.treeprocessors.register(
            MkdocsMdpoTitlesTreeProcessor(self),
            'mkdocs-mdpo-tree-titles',
            -88888,
        )
