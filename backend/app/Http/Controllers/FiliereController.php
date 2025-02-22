<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\FiliereModel;

class FiliereController extends Controller
{
   public function getFilieres(Request $request)
   {
    $filiers =FiliereModel::all();
    return $filiers;

   }
}
