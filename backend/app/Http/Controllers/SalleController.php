<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\SalleModel;

class SalleController extends Controller
{
   public function getSalles(Request $request)
   {
    $salles = SalleModel::all(); 
    return $salles;

   }
}
