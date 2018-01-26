const gulp = require('gulp');
const shell = require('gulp-shell');

const create_virtual_environment = [
  'virtualenv .virtual\n',
  'source .virtual/bin/activate && pip install -r requirements.txt && deactivate\n'
];

const create_local_runtime_variables = [
  'cp ./env/local .env\n'
];
gulp.task('install', shell.task([].concat(
  create_virtual_environment,
  create_local_runtime_variables
).join('')));

gulp.task('pip', shell.task((function pip(){
  if(process.argv[3]=='-i'){
    // install 4th element
    return 'source .virtual/bin/activate && pip install '+process.argv[4] + ' && deactivate';
  }
}())));

gulp.task('test', shell.task([
  'echo "testing not setup yet"'
].join('')));


