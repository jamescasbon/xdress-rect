import os
clang_includes = [os.path.expanduser('~/Src/llvm/Debug+Asserts/lib/clang/3.4/include')]

package = 'rect'
classes = [
    ('Rectangle', 'src/rectangle.*')
]
