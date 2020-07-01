#include <stdio.h>
#include <string.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *args[])
{
printf("##########################\n##########################\n");
//    char name[10] = "car";
//
//    char test[50] = "car";
//
//    int result = strcmp(name,test);
//	if(result==0){
//	system("python3 mortor_ver2.py");
//    }
int class_id = 2;
int width = 250;
int th = 200;
if(class_id==2){
if(width > th){
	system("python3 /home/signal/Desktop/darknet-spiedv2/src/mortor_ver2.py");
	printf("##########################\n##########################\n");
	sleep(2);
}
}

    return 0;
}
