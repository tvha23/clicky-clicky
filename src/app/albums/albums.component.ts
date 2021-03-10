import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { HttpClient } from '@angular/common/http';
import { AlbumInterface } from './AlbumInterface';
import { Router } from '@angular/router';


@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})

export class AlbumsComponent implements OnInit {
  
  albums:Array<AlbumInterface>;
  constructor(private dataService: DataService, private router:Router  ) { }

  ngOnInit(): void {
    this.dataService.sendGetRequest().subscribe((data: Array<AlbumInterface>) => {
      console.log(data);
      this.albums=data;
    })
  }
  onSelect(album):void{
    this.router.navigate(['/albums', album.id])
  }
}

