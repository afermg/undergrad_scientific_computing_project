//Mínimos Cuadrados
//Programa hecho por Alan Muñoz

#include <stdio.h>
#include "math.h"
#include <stdlib.h>

double pow(double x, double y);
float powf(float x, float y);
long double powl(long double x, long double y);

int main(){
int puntos;
scanf("%d", &puntos);
int *pun_x;
int *pun_y;
pun_x = (int*)malloc(sizeof(int)*puntos);
pun_y = (int*)malloc(sizeof(int)*puntos);

int grado,i,j,k,n,m,temp; //Contadores y variable temporal para elevar x's a las potencias

for (i=0;i<puntos;i++){
	scanf("%d", (pun_x+i));
	scanf("%d", (pun_y+i));
} 

printf("Introduce el grado del polinomio que quieres obtener: ");
scanf("%d", &grado);

int *suma_x;
int *suma_y;
double **matriz;

suma_x = (int*)malloc((2*grado)*sizeof(int));
suma_y = (int*)malloc((grado+1)*sizeof(int));
matriz = (double**)malloc((grado+1)*sizeof(double*));

for(i=0;i<grado+2;i++){//Creamos e imprimimos el vector de las sumas de x**n
	*(suma_x+i)=0; 
	for(j=0;j<puntos;j++){
		temp = pow(*(pun_x+j),i);
		*(suma_x+i)+= *(pun_x+j)*temp;
	}
	
	printf("%d",*(suma_x+i));
	printf("\t");
}

printf("\n");
for(i=0;i<grado+1;i++){//Creamos e imprimimos el vector de las sumas de y*x**n
	
	*(suma_y+i)=0;
	for (j=0;j<puntos;j++){
		temp = pow(*(pun_x+j),i);
		*(suma_y+i)+=*(pun_y+j)*temp;
	}
	printf("%d",*(suma_y+i));
	printf("\t");
}

printf("\n");
for(i=0;i<grado+1;i++){//Introducimos los valores a la matriz 1. De 0 a 2
	*(matriz+i) = (double*)malloc(sizeof(double)*(grado+2));
	*(*(matriz+i)+(grado+1)) = *(suma_y+i);//matriz[i][grado+1]=suma_y[i]
	for(j=0;j<grado+1;j++){//De 0 a 2
		if (i==0 && j==0) **matriz=puntos;//Si i y j = 0 es valor n
		else *(*(matriz+i)+j)= *(suma_x+j+i-1);//Sino matriz[i][j]=suma_x[j+i-1]
	}
}


printf("\n");
for(i=0;i<grado+1;i++){//Imprimimos la matriz Original
	for(j=0;j<grado+2;j++){
		if (j) printf("\t");
		printf("%lf",*(*(matriz+i)+j));
	}
	printf("\n");
}

for(i=0;i<grado;i++){
	for(j=i+1;j<grado+1;j++){
		for(k=0;k<grado+2;k++){
			*(*(matriz+j)+k) -= *(*(matriz+i)+k)* *(*(matriz+i)+j)/ *(*(matriz+i)+i);
			printf("%lf\n",*(*(matriz+i)+j));
		}
	}
	
	printf("\n\n");
for(n=0;n<grado+1;n++){
	for(m=0;m<grado+2;m++){
		if (m) printf("\t");
		printf("%lf",*(*(matriz+n)+m));
	}
	printf("\n");
}

}

for(i=grado;i;i--){
	for(j=i-1;j>=0;j--){
		for(k=grado+1;k>=i;k--){
			*(*(matriz+j)+k) -= *(*(matriz+i)+k)* *(*(matriz+j)+i)/ *(*(matriz+i)+i);
		}
	}
	
	printf("\n\n");
for(n=0;n<grado+1;n++){
	for(m=0;m<grado+2;m++){
		if (m) printf("\t");
		printf("%lf",*(*(matriz+n)+m));
	}
	printf("\n");
}

}

printf("\na's:\n");
for(i=0;i<grado+1;i++){
	printf("a%d = %lf\n",i,*(*(matriz+i)+grado+1)/ *(*(matriz+i)+i));
}

free(pun_x);
free(pun_y);
free(suma_x);
free(suma_y);
free(matriz);
return 0;
}
