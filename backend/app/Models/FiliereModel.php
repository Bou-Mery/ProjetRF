<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class FiliereModel extends Model
{
    protected $table = 'filiere';
    /**
     * Indique si les horodatages sont utilisés pour le modèle.
     *
     * @var bool
     */
    public $timestamps = false;
    
    }
