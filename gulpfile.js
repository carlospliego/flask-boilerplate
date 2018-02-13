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

gulp.task('env', shell.task([].concat(
  create_local_runtime_variables
).join('')));

gulp.task('unit', shell.task([
  'export $(cat .env | xargs) && .virtual/bin/coverage run --source=src -m unittest discover -s src\n',
  '.virtual/bin/coverage html\n'
].join('')));

gulp.task('newman', shell.task([].concat(
  [
    'docker-compose up mongo-seed\n',
    'newman run ./postman/flask.postman_collection.json\n',
    'docker-compose up mongo-seed'
  ]
).join('')));

gulp.task('test', shell.task([
  'gulp newman\n',
  'gulp unit'
].join('')));

gulp.task('w', function(){
  gulp.watch('src/**/*.py', ['unit'])
});

