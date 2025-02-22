<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ComptModel;
use App\Models\ProfModel;

class ProfController extends Controller
{
    public function storeCompte(Request $request)
    {
        // Validation des données
        $validatedData = $request->validate([
            'cin' => 'required',
            'username' =>'required',
            'password' =>'required',
        ]);
        
        // Création d'un nouveau compte
        $compte = new ComptModel();
        $compte->username = $validatedData['username'];
        $compte->password = $validatedData['password'];  
        $compte->cin = $validatedData['cin'];
        $compte->save();

    
    }


    public function getProfesseur(Request $request)
    {
        $professeurs = ProfModel::all();
        return $professeurs;
    }
}
