import {EventEmitter} from '@angular/core'

export class Emitters {
    //to access them directly it is static
    static authEmitter = new EventEmitter<boolean>();
}