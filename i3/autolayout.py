#!/usr/bin/python3

from itertools import takewhile

import i3ipc # https://github.com/acrisci/i3ipc-python

def ancestors(con):
    it = con.parent
    while it:
        yield it
        it = it.parent

def find_stack(con):
    stacks = [ancestor
        for ancestor in takewhile(lambda x: x.type != 'workspace',
                                  ancestors(con))
        if ancestor.layout in ['stacked', 'tabbed']]
    return (stacks or [None])[-1]

def on_new_window(self, e):
    aux = i3ipc.Connection()
    new_con = aux.get_tree().find_by_id(e.container.id)
    orig_stack = find_stack(new_con)
    if not orig_stack:
        return
    workspace = orig_stack.parent

    orig_stack_n = workspace.nodes.index(orig_stack)
    dest_stack_n = (orig_stack_n + 1) % len(workspace.nodes)
    dest_stack = workspace.nodes[dest_stack_n]

    dest_stack.command('mark dest')
    new_con.command('move container to mark dest, focus')
    aux.command('unmark dest')

i3 = i3ipc.Connection()
i3.on('window::new', on_new_window)
i3.main()