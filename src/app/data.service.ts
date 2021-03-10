import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AlbumInterface } from './albums/AlbumInterface';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private REST_API_SERVER = "https://jsonplaceholder.typicode.com/albums";

  constructor(private httpClient: HttpClient) { }

  public sendGetRequest()
  {
    return this.httpClient.get(this.REST_API_SERVER);
  }
}
