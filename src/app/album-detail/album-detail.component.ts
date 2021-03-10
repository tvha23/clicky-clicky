import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumInterface } from '../albums/AlbumInterface';
import { DataService } from '../data.service';
import { HttpClient } from '@angular/common/http';
import {Location} from '@angular/common';


@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  albumId:number;
  albums:Array<AlbumInterface>;
  constructor(private dataService: DataService, private route:Router, private r:ActivatedRoute, private _location: Location) { }

  backClicked() {
    this._location.back();
  }
  ngOnInit(): void {
    this.dataService.sendGetRequest().subscribe((data:Array<AlbumInterface>) => {
      this.r.paramMap.subscribe(params=>{
        let id=+params.get('id');
      this.albumId=id-1;
      // console.log(id);
      });
      // console.log(data);
      this.albums=data;
  }
    )
}
}