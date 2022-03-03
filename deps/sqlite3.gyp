# ===
# This configuration defines options specific to compiling SQLite3 itself.
# Compile-time options are loaded by the auto-generated file "defines.gypi".
# The --sqlite3 option can be provided to use a custom amalgamation instead.
# ===

{
  'includes': ['common.gypi'],
  'targets': [
    {
      'target_name': 'sqlite3',
      'type': 'static_library',
      'sources': ['sqlite3/sqlite3.c'],
      'include_dirs': ['sqlite3/'],
      'direct_dependent_settings': {
        'include_dirs': ['sqlite3/'],
      },
      'cflags': ['-std=c99', '-w'],
      'xcode_settings': {
        'OTHER_CFLAGS': ['-std=c99'],
        'WARNING_CFLAGS': ['-w'],
      },
      'conditions': [
        ['sqlite3 == ""', {
          'includes': ['defines.gypi'],
        }, {
          'defines': [
            # This is currently required by better-sqlite3.
            'SQLITE_ENABLE_COLUMN_METADATA',
          ],
        }]
      ],
      'configurations': {
        'Debug': {
          'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 1 } }, # static debug
        },
        'Release': {
          'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 0 } }, # static release
        },
      },
    },
  ],
}
