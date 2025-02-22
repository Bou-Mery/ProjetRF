<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\EtudiantController;
use App\Http\Controllers\TestStudentController;
use App\Http\Controllers\AdmincompteController;
use App\Http\Controllers\ProfController;
use App\Http\Controllers\SalleController;
use App\Http\Controllers\ModuleController;
use App\Http\Controllers\FiliereController;

Route::get('/etudiants',[EtudiantController::class ,'give']);
Route::post('/enrg',[TestStudentController::class,'store']);
Route::post('/adminconnection',[AdmincompteController::class,'verify']);
Route::get('/filiere',[TestStudentController::class,'filiere']);
Route::get('/allstudents',[TestStudentController::class,'students']);
Route::post('/addprofc',[ProfController::class,'storeCompte']);
Route::get('/getprof',[ProfController::class,'getProfesseur']);
Route::get('/getsalle',[SalleController::class,'getSalles']);
Route::get('/getmodules',[ModuleController::class,'getmodules']);
Route::get('/getfilieres',[FiliereController::class,'getFilieres']);



/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});
