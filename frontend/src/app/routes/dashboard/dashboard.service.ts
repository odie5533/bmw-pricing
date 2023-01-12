import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ChartData {
  items: any[];
}

@Injectable()
export class DashboardService {
  constructor(private http: HttpClient) {}

  getCharts(): Observable<ChartData> {
    return this.http.get<ChartData>('http://127.0.0.1:5000/api/v1/carsale/summary');
  }
}
