const gulp = require('gulp');
const shell = require('gulp-shell');

const create_virtual_environment = [
  'virtualenv -p python3 .virtual\n',
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
    return 'source .virtual/bin/activate && pip install '
      +process.argv[4] + ' && pip freeze > requirements.txt && deactivate';
  }
}())));

gulp.task('unit', shell.task([
  'source .virtual/bin/activate && python -m unittest discover -s src\n'
].join('')));

gulp.task('unit-w', function(){
  gulp.watch('src/**/*.py', ['test'])
});

