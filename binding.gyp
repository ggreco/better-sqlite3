# ===
# This is the main GYP file, which builds better-sqlite3 with SQLite3 itself.
# ===

{
  'targets': [
    {
      'includes': ['deps/common.gypi', 'deps/defines.gypi'],
      'target_name': 'better_sqlite3',
      'sources': ['deps/sqlite3/sqlite3.c', 'src/better_sqlite3.cpp'],
      'include_dirs': ['deps/sqlite3/'],
      'cflags': ['-std=c++14'],
      'xcode_settings': {
        'OTHER_CFLAGS': ['-std=c99'],
        'OTHER_CPLUSPLUSFLAGS': ['-std=c++14', '-stdlib=libc++'],
        'WARNING_CFLAGS': ['-w'],
      },
      'conditions': [
        ['OS=="linux"', {
          'ldflags': [
            '-Wl,-Bsymbolic',
            '-Wl,--exclude-libs,ALL',
          ],
        }],
      ],
      'configurations': {
        'Debug': {
          'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 1 } }, # static debug
        },
        'Release': {
          'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 0 } }, # static release
        },
      },
    }
  ],
}
