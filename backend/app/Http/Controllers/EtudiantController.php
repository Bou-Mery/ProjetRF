<?php

namespace App\Http\Controllers;

use App\Models\Etudiant; // Importation correcte de la classe Etudiant
use Illuminate\Http\Request;

class EtudiantController extends Controller
{
    public function give(Request $request)
    {  
        $idfil = $request->query('idfil');
        $etudiants = Etudiant::where('idFiliere', $idfil)
                             ->select('cne', 'nom', 'prenom', 'idFiliere')
                             ->get();
        return $etudiants;
    }

   
}
