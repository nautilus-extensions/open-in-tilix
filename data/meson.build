install_data('open-in-tilix.appdata.xml', install_dir: join_paths(
    get_option('datadir'), 
    'appdata')
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', join_paths(
    get_option('datadir'), 
    'appdata', 'open-in-tilix.appdata.xml')]
  )
endif
