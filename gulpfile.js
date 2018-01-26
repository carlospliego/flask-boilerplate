const gulp = require('gulp');
const shell = require('gulp-shell');

const create_virtual_environment = [
  '. ./dev/settings.sh\n',
  'virtualenv .virtual\n',
  '. .virtual/bin/activate && pip install -r requirements.txt && deactivate\n'
];

const create_docker_files = [
  'source dev/settings.sh; rm -rf docker-compose.yml; envsubst < "dev/file_templates/docker/docker-compose.yml" > "docker-compose.yml";\n',
  'source dev/settings.sh; rm -rf dev.Dockerfile; envsubst < "dev/file_templates/docker/dev.Dockerfile" > "dev.Dockerfile";\n',
  'source dev/settings.sh; rm -rf prod.Dockerfile; envsubst < "dev/file_templates/docker/prod.Dockerfile" > "prod.Dockerfile";\n',
  'source dev/settings.sh; rm -rf .dockerignore; envsubst < "dev/file_templates/docker/.dockerignore" > ".dockerignore";\n'
];

const create_local_runtime_variables = [
  'cp ./dev/file_templates/env/local .env\n'
];
gulp.task('install', shell.task([].concat(
  create_virtual_environment,
  create_docker_files,
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


