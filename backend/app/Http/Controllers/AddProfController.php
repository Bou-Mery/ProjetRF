<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ComptModel;
use App\Models\ProfModel;

class AddProfController extends Controller
{
    public function storeProf(Request $request)
    {
        $request->validate([
            'nom' => 'required',
            'cin' => 'required',
            'username' =>'required',
            'password' =>'required',
            'prenom' => 'required'
        ]);
        $compte = new Compte();
        $compte->username = $request->username;
        $compte->password = $request->password;  
        $compte->save();

        $infocompte = Compte::where($username,$request->username)
                            ->where($password,$request->password)  
                            ->first();
        
        $professeur=new ProfModel();
        $professeur->cin =$request->cin;
        $professeur->nom = $request->nom;
        $professeur->prenom = $request->prenom;
        $professeur->tel = $request->tel;
        $professeur->idCompte = $infocompte->idCompte;
        $professeur->save();

    }
}
