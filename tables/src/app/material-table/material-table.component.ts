// material-table.component.ts
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator'; 
import { MatTableDataSource } from '@angular/material/table';
import { MatDialog } from '@angular/material/dialog';
import { ThisReceiver } from '@angular/compiler';

interface PeriodicElement {
  productid: number;
  name: string;
  description: string;
  quantity: number;
  stock: number;
  price: number;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {productid: 1, name: 'Apple', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 2, name: 'Orange', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 3, name: 'Grapes', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 4, name: 'Banana', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 5, name: 'Mango', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 6, name: 'Pomegranate', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 7, name: 'Papaya', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 8, name: 'Watermelon', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 9, name: 'Pineapple', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 10, name: 'Guava', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 11, name: 'Strawberry', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 12, name: 'Jackfruit', description: ' Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 13, name: 'Kiwi', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 14, name: 'Lychee', description: 'Fruit', quantity: 0, stock: 10, price: 10},
  {productid: 15, name: 'cherry', description: 'Fruit', quantity: 0, stock: 10, price: 10},
];
const ELEMENT_DATA1: PeriodicElement[] = [
];

@Component({
  selector: 'app-material-table',
  templateUrl: './material-table.component.html',
  styleUrls: ['./material-table.component.css']
})
export class MaterialTableComponent implements OnInit {

  dataSourceOne: MatTableDataSource<PeriodicElement>;
  displayedColumnsOne: string[] = ['productid', 'name', 'description','price', 'action'];
  @ViewChild('TableOnePaginator', { static: true })
  tableOnePaginator!: MatPaginator;
  @ViewChild('TableOneSort', { static: true })
  tableOneSort!: MatSort;


  dataSourceTwo: MatTableDataSource<PeriodicElement>;
  displayedColumnsTwo: string[] = ['productid', 'name', 'description','price','quantity','amount'];
  @ViewChild('TableTwoPaginator', { static: true })
  tableTwoPaginator!: MatPaginator;
  @ViewChild('TableTwoSort', { static: true })
  tableTwoSort!: MatSort;

  constructor(public dialog:MatDialog) {
    this.dataSourceOne = new MatTableDataSource;

    this.dataSourceTwo = new MatTableDataSource;
  }

  ngOnInit() {
    this.dataSourceOne.data = ELEMENT_DATA;
    this.dataSourceOne.paginator = this.tableOnePaginator;
    this.dataSourceOne.sort = this.tableOneSort;

    this.dataSourceTwo.data = ELEMENT_DATA1;
    this.dataSourceTwo.paginator = this.tableTwoPaginator;
    this.dataSourceTwo.sort = this.tableTwoSort;
  }

  applyFilterOne(filterValue: string) {
    this.dataSourceOne.filter = filterValue.trim().toLowerCase();
  }

  applyFilterTwo(filterValue: string) {
    this.dataSourceTwo.filter = filterValue.trim().toLowerCase();
  }
  addtocart(element: PeriodicElement)
  {
    if(!ELEMENT_DATA1.includes(element))
    {
      element.quantity=1;
      ELEMENT_DATA1.push(element);
      this.dataSourceTwo.data=ELEMENT_DATA1;
    }

  }
  minusquantity(element: PeriodicElement)
  {
    if(element.quantity==1)
    {
      ELEMENT_DATA1.forEach((value,index)=>{
        if(value==element) ELEMENT_DATA1.splice(index,1);
      });
      this.dataSourceTwo.data=ELEMENT_DATA1;
    }
    else
    {
      element.quantity=element.quantity-1;
    }
  }
  plusquantity(element: PeriodicElement)
  {
    element.quantity=element.quantity+1;    
  }
  getTotalCost()
  {
    return(ELEMENT_DATA1.reduce((subtotal, item) => subtotal + item.quantity * item.price,0))
  }
}
