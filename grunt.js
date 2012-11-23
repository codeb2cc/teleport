module.exports = function (grunt) {
  grunt.loadNpmTasks('grunt-css')

  grunt.initConfig({
    meta: {
      banner: '/*! <%= grunt.template.today("yyyy-mm-dd HH:MM") %>\n' +
        ' *  Copyright (c) <%= grunt.template.today("yyyy") %> codeb2cc.com\n' +
        ' */'
    },
    concat: {
      auth: {
        src: ['<banner>', 'assets/js/src/common.js', 'assets/js/src/security.js', 'assets/js/src/auth.js'],
        dest: 'assets/js/auth-debug.js'
      },
      panel: {
        src: ['<banner>', 'assets/js/src/common.js', 'assets/js/src/panel.js'],
        dest: 'assets/js/panel-debug.js'
      }
    },
    min: {
      auth: {
        src: ['<banner>', 'assets/js/auth-debug.js'],
        dest: 'assets/js/auth.js'
      },
      panel: {
        src: ['<banner>', 'assets/js/panel-debug.js'],
        dest: 'assets/js/panel.js'
      }
    },
    cssmin: {
      app: {
        src: ['<banner>', 'assets/css/app.css'],
        dest: 'assets/css/app.min.css'
      }
    }
  })

  grunt.registerTask('default', 'concat min cssmin')
}
