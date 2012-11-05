module.exports = function (grunt) {
  grunt.initConfig({
    meta: {
      banner: '/*! <%= grunt.template.today("yyyy-mm-dd HH:MM") %>\n' +
        ' *  Copyright (c) <%= grunt.template.today("yyyy") %> codeb2cc.com\n' +
        ' */'
    },
    concat: {
      dist: {
        src: ['<banner>', 'assets/js/src/app.js'],
        dest: 'assets/js/app-debug.js'
      }
    },
    min: {
      dist: {
        src: ['<banner>', 'assets/js/app-debug.js'],
        dest: 'assets/js/app.js'
      }
    }
  })

  grunt.registerTask('default', 'concat min')
}
