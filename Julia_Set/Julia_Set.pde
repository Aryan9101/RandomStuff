int initZ = 0;
float constantReal, constantImag = 0;
int iterations = 100;
int bound  = 16;

void setup(){
  size(500, 500);
  colorMode(RGB, 1);
}

void draw(){
  background(255);
  loadPixels();
  int i, j, k = 0;
  float x = map(mouseX, 0, width, 0, 2*PI);
  float y = map(mouseY, 0, height, 0, 1);
  constantReal = y * euler(x)[0];
  constantImag = y * euler(x)[1];
  for (j = 0; j < height; j++){
  
    for (i = 0; i < width; i++){
    
      boolean flag = true;
      
      float a = map(i, 0, width, -2, 2);
      float b = map(j, 0, height, -2, 2);
      
      //float constantReal = a;
      //float constantImag = b;
      
      for (k = 0; k < iterations; k++){
      
        float real = a * a - b * b;
        float imag = 2 * a * b;
        
        a = real + constantReal;
        b = imag + constantImag;
        
        if(a*a + b*b > bound){
          flag= false;
          break;
        }  
      }
      
      if (flag){
        pixels[i + j*width] = color(0);
      } else {
        pixels[i + j*width] = color(sqrt(float(k) / iterations));
      }
    }
  }
  updatePixels();
}

float[] euler(float x){
  float[] cis = {cos(x), sin(x)};
  return cis;
}  
