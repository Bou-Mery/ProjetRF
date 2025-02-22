<?php

namespace App\Http\Controllers;
use App\Models\AdminCompte;
use Illuminate\Http\Request;

class AdmincompteController extends Controller
{  
    
    public function verify(Request $request)
    {
        $comptes = AdminCompte::where('username',$request->username) 
                                ->where('password',$request->password)
                                ->first();
        if($comptes) {
                return response()->json(['message'=>'trouve']);
        }
        return response()->json(['message'=>'introuvable']);

    }
}
