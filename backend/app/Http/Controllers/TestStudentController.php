<?php

namespace App\Http\Controllers;
use App\Models\TestStudent;
use App\Models\FiliereModel;
use Illuminate\Http\Request;

class TestStudentController extends Controller
{
    public function store(Request $request)
    {   
        $data=$request->all();
        $etudianttest = new TestStudent; 
        $etudianttest->nom = $data['nom'];
        $etudianttest->prenom = $data['prenom'];
        $etudianttest->age = $data['age'];
        $etudianttest->dept = $data['dept'];
        $etudianttest->image = $data['image'];
        $etudianttest->save();

        
    }
    public function filiere(Request $request)
    {
        $filiere=FiliereModel::all();
        return $filiere;
    }
    public function students(Request $request)
    {
        $students = TestStudent::all();
        return $students;
    }
}
