<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ModuleModel;

class ModuleController extends Controller
{   
    public function getModules(Request $request)
    {
        $idfil = $request->query('idfil');
        $modules = ModuleModel::where('idFiliere',$idfil)->get();
        return $modules;
    }
}
