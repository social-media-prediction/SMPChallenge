var gulp = require('gulp');
var watch = require('gulp-watch');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var uglify = require('gulp-uglify');
var pump = require('pump');
var browserSync = require('browser-sync').create();
var reload      = browserSync.reload;
var spritesmith = require("gulp-spritesmith");
var concat = require('gulp-concat');

gulp.task('sass', function () {

    return gulp.src("./src/scss/*.scss")
        .pipe(watch('./src/scss/*.scss'))
        .pipe(sass({outputStyle:'compressed'}).on('error', sass.logError))
        .pipe(gulp.dest('./dist/css'))
        .pipe(reload({stream: true}));
});

gulp.task('autoprefixer', function () {
    return gulp.src('./dist/css/*.css')
        .pipe(watch('./dist/css/*.css'))
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe(gulp.dest('./dist/css'));
});

gulp.task('compress', function (cb) {
    pump([
            gulp.src('./src/js/*.js'),
            uglify(),
            gulp.dest('./dist/js')
        ],
        cb
    );
});
//合并js
gulp.task('scripts', function() {
    return gulp.src(['./dist/js/mobiscroll.core.js', './dist/js/mobiscroll.widget.js', './dist/js/mobiscroll.scroller.js', './dist/js/mobiscroll.util.datetime.js', './dist/js/mobiscroll.datetimebase.js', './dist/js/mobiscroll.widget.ios.js','./dist/js/mobiscroll.i18n.zh.js'])
        .pipe(concat('datepicker.js'))
        .pipe(gulp.dest('./dist/js'));
});
gulp.task('browser-sync', function() {

    browserSync.init({
        server: "./"
    });

    gulp.watch("./src/scss/*.scss", ['sass','autoprefixer']);
    gulp.watch("./src/js/*.js", ['compress']);
    gulp.watch(["*.html","./view/*.html"]).on('change', reload);

});

gulp.task('spritesmith',function(){
    gulp.src('./img/*.png')
        .pipe(spritesmith({
            destImg: './dist/img/icon-sprite.png',
            destCSS: './dist/css/icon-sprite.css'
        }));
});

gulp.task('default', ['browser-sync','sass','autoprefixer']);