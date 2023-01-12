import { Component, OnInit, OnDestroy, ChangeDetectionStrategy, ChangeDetectorRef, AfterViewInit, NgZone } from '@angular/core';
import { DashboardService } from './dashboard.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [DashboardService],
})
export class DashboardComponent implements OnInit, AfterViewInit, OnDestroy {
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];

  isLoading = true;

  charts: any;
  chart1: any;
  chart2: any;

  constructor(
    private ngZone: NgZone,
    private dashboardSrv: DashboardService,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit() {
    this.getChartData();
  }

  ngAfterViewInit() {
  }

  ngOnDestroy() {
    if (this.chart1) {
      this.chart1?.destroy();
    }
    if (this.chart2) {
      this.chart2?.destroy();
    }
  }

  getChartData() {
    this.dashboardSrv.getCharts().subscribe(res => {
      this.charts = res;
      console.log(res);
      this.cdr.detectChanges();
      this.ngZone.runOutsideAngular(() => this.initChart());
    },
      (err: any) => {
        this.isLoading = false;
        console.log(err);
      },
      () => {
        this.isLoading = false;
        this.cdr.detectChanges();
      }
    );
  }

  initChart() {
    const fuel_types = Object.keys(this.charts["fuel"]);
    const fuel_sales = Object.values(this.charts["fuel"]);
    const paint_colors = Object.keys(this.charts["paint_color"]);
    const paint_sales = Object.values(this.charts["paint_color"]);
    const charts = [
        {
          chart: {
            height: 350,
            type: 'bar',
            toolbar: false,
          },
          dataLabels: {
            enabled: true,
          },
          stroke: {
            curve: 'smooth',
          },
          series: [
            {
              name: 'Sales',
              data: paint_sales,
            },
          ],
          xaxis: {
            categories: paint_colors,
          },
          legend: {
            position: 'top',
            horizontalAlign: 'right',
          },
        },
        {
          chart: {
            height: 350,
            type: 'bar',
            toolbar: false,
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            curve: 'smooth',
          },
          series: [
            {
              name: 'Sales',
              data: fuel_sales,
            },
          ],
          xaxis: {
            categories: fuel_types,
          },
          legend: {
            position: 'top',
            horizontalAlign: 'right',
          },
          plotOptions: {
            bar: {
              horizontal: true
            }
          },
          tooltip: {
            enabled: true,
          }
        },
    ];
    this.chart1 = new ApexCharts(document.querySelector('#chart1'), charts[0]);
    this.chart1?.render();
    this.chart2 = new ApexCharts(document.querySelector('#chart2'), charts[1]);
    this.chart2?.render();
  }
}
