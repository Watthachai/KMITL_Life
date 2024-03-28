/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2021 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "adc.h"
#include "dma.h"
#include "rng.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
/*-------------------------------FLAPPY BIRD ---------------------------------*/

#include "stdio.h"
#include "ILI9341_Touchscreen.h"
#include "ILI9341_STM32_Driver.h"
#include "ILI9341_GFX.h"

/*-------------------------------END FLAPPY BIRD ---------------------------------*/
#include "string.h"
#include <stdbool.h>
//#include "picture.h"
/*-------------------------------FLAPPY ---------------------------------*/
#define WIDTH_PILL        40

#define HIDDENT            50

#define HEIGH_SCREEN     235

#define DISTANCE        80

#define YES                1
#define NO                0

#define WIDTH_BIRD        26
#define HEIGH_BIRD          19

#define WIDTH_LINE        320
#define HEIGH_LINE        5

#define BIRD_X            110
#define BIRD_Y            100

#define X_COM           136

#define FALLING            0
#define RISING            1

#define X_SCORE            75
#define Y_SCORE            223
#define X_H_SCORE        110

#define X_GAME_OVER        100
#define Y_GAME_OVER        40

#define X_GAME_H_SCORE  85
#define Y_GAME_H_SCORE  70

#define X_GAME_SCORE    115
#define Y_GAME_SCORE    100

#define X_SOCRE_END        185
#define X_SCORE_H_END    215
#define SCORED            69

#define X_BUT            90
#define Y_BUT            130

/*-------------------------------END FLAPPY BIRD ---------------------------------*/


/*-------------------------------PING PONG ---------------------------------*/


/*-------------------------------END PING PONG ---------------------------------*/



uint16_t list_heigh[15];

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
/*--------------------------------PING PONG -----------------------------------*/
volatile adc_value = 0 ;
volatile adc_value_2 = 0 ;
char score_sender[20] = "";
bool game_running = false;
bool reset_game = false;
char str[100] ;
char str1[] = "\r\n";
char str2[] = "PD4 HAS BEEN PRESS\r\n";
char str3[] = "Game Running\r\n";
uint8_t player_1_score = 0 ;
uint8_t player_2_score = 0 ;
char str_player_1[] = "1";


uint16_t ball_color = BLACK; // Initial color: red


//Paddle Size
uint8_t paddle_1_x1 = 60 ;
uint8_t paddle_1_x2 = 65 ;
uint8_t paddle_1_y1 = 78 ;
uint8_t paddle_1_y2 = 133;
uint8_t oldpaddle_1_x1, oldpaddle_1_x2, oldpaddle_1_y1, oldpaddle_1_y2;


//Paddle 2 Size
uint8_t paddle_2_x1 = 240;
uint8_t paddle_2_x2 = 245;
uint8_t paddle_2_y1 = 78 ;
uint8_t paddle_2_y2 = 133;
uint8_t oldpaddle_2_x1, oldpaddle_2_x2, oldpaddle_2_y1, oldpaddle_2_y2;


//ball location
uint8_t ball_x = 150;
uint8_t ball_y = 100;
uint8_t ballDirectionX = 1;
uint8_t ballDirectionY = 1;
uint8_t oldball_x, oldball_y;
//DEFIND SCREEN

uint32_t screen_hight = 250;
uint32_t screen_width = 240;


HAL_StatusTypeDef status;

/*--------------------------------END PING PONG -----------------------------------*/

/* Private variables ---------------------------------------------------------*/

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */
/* Private function prototypes -----------------------------------------------*/


/*-------------------------------FLAPPY BIRD ---------------------------------*/

#include "line.h"
#include "button.h"
#include "image.h"
void Init_Game();
void Draw_Pillar(int16_t x, uint16_t heigh);
void Init_Heigh_Pill();
void Bird_Fly(uint16_t y);
void Convert_To_String(uint16_t val);
void Print_Score(uint16_t, uint16_t x_score, uint16_t color);
void Game_Over();
int Button_Press(uint16_t x, uint16_t y, uint16_t width, uint16_t heigh);
void Welcome();
void Click_Here();
uint16_t score = 0; 
uint16_t high_score = 0;


int16_t x1 = 0, x2 = 0;	

uint16_t heigh_pill1 = 0;	
uint16_t heigh_pill2 = 0;

int16_t y_bird = 0;

uint16_t x_com = 0;
uint16_t h_com = 0;

int gamestate = 0;
int checkstartflappy = 0;
int checkstartpong = 0;
int additionalButtonPress = 0;

int current_delay = 10; // ค่า delay เริ่มต้น
int delay_levels[] = {50, 20, 1}; // ระดับ delay
int delay_index = 1; // ค่า index ในอาร์เรย์ของ delay_levels
int button_state = 0;   // เ�?็บสถานะปุ่ม PF13

/*-------------------------------END FLAPPY BIRD ---------------------------------*/

/*-------------------------------PING PONG ---------------------------------*/
uint16_t CRC16_2(uint8_t *,uint8_t);

/*-------------------------------END PING PONG ---------------------------------*/
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */
/* Enable the CPU Cache */

  /* Enable I-Cache---------------------------------------------------------*/
  SCB_EnableICache();

  /* Enable D-Cache---------------------------------------------------------*/
  SCB_EnableDCache();

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_SPI5_Init();
  MX_TIM1_Init();
  MX_RNG_Init();
  MX_ADC1_Init();
  MX_TIM3_Init();
  MX_USART3_UART_Init();
  MX_ADC2_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */

  ILI9341_Init();
  ILI9341_Fill_Screen(BLACK);
/*-------------------------FLAPPY BRID----------------------------------*/
  


  /*-------------------------END FLAPPY BRID----------------------------------*/

  /*-------------------------PING PONG ----------------------------------*/
    ILI9341_Set_Rotation(SCREEN_HORIZONTAL_2);


    HAL_ADC_Start(&hadc1);
    HAL_ADC_Start(&hadc2);
    /*-------------------------END PING PONG----------------------------------*/
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */

  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
	  /*-------------------------FLAPPY BRID----------------------------------*/
	  if (HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_7) == GPIO_PIN_RESET) {
	      HAL_Delay(70);


	      if (HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_7) == GPIO_PIN_RESET) {

	          if (gamestate == 0) {
	            checkstartpong = 0;
	            gamestate = 1;
	          } else if (gamestate == 1){
	              checkstartflappy = 0;
	        	  gamestate = 0;

	          }
	      }
	  }


	  if (gamestate == 0) {
	      Start_GameFlappy();
	  }
	  if (gamestate == 1) {
	      StartGamePingpong();

	  }



	  /*-------------------------FLAPPY BRID----------------------------------*/

	  /*-------------------------PING PONG----------------------------------*/


	 	  }
	  /*-----------------------END PING PONG----------------------------------*/


  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure LSE Drive Capability
  */
  HAL_PWR_EnableBkUpAccess();

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_BYPASS;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 4;
  RCC_OscInitStruct.PLL.PLLN = 200;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 9;
  RCC_OscInitStruct.PLL.PLLR = 2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Activate the Over-Drive mode
  */
  if (HAL_PWREx_EnableOverDrive() != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_6) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */

/*-----------------------------Interrupt-----------------------------------------------*/

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) {
   HAL_GPIO_EXTI_IRQHandler(GPIO_PIN_13);
	if (GPIO_Pin == GPIO_PIN_13) {
        HAL_NVIC_SystemReset(); // Reset บอร์ด
    }
}

/*-----------------------------END Interrupt-------------------------------------------*/
/*------------------------------------FLAPPY BIRD--------------------------------------*/


void Init_Heigh_Pill(){
	int i =0;
	int value = 0;
	for(i=0; i<15; i++){
		list_heigh[i] = 150-value;
		value += 10;
	}
}

void WelcomeFlappy(){
	ILI9341_Set_Rotation(SCREEN_HORIZONTAL_2);
	ILI9341_Fill_Screen(WHITE);
	ILI9341_Draw_Text("Flappy Bird",60, 40,BLACK,3,WHITE);

	ILI9341_Draw_Filled_Circle(80, 150, 10, YELLOW);
	ILI9341_Draw_Text(":change game", 100, 140, BLACK, 2, WHITE);

	ILI9341_Draw_Filled_Circle(80, 180, 10, DARKGREEN);
	ILI9341_Draw_Text(":start game", 100, 170, BLACK, 2, WHITE);

	ILI9341_Draw_Filled_Circle(30, 210, 10, RED);
	ILI9341_Draw_Text(":change difficulty",50 , 200, BLACK, 2, WHITE);

}

void Draw_Pillar(int16_t x, uint16_t height) {
    if (x < 321) {
       
        int16_t x1 = x + WIDTH_PILL + 1;

        ILI9341_Draw_Vertical_Line(x1, 1, height, WHITE);
        ILI9341_Draw_Vertical_Line(x1, 1+height+DISTANCE, HEIGH_SCREEN, WHITE);

        ILI9341_Draw_Vertical_Line(x, 1, height, GREEN);
        ILI9341_Draw_Vertical_Line(x, 1+height+DISTANCE, HEIGH_SCREEN, GREEN);
    }
}



void Bird_Fly(uint16_t y) {
    ILI9341_Fill_Color(BIRD_X, y - 3, BIRD_X + WIDTH_BIRD + 5, y + HEIGH_BIRD + 5, WHITE);
    HAL_Delay(1);
    ILI9341_Write_Pic_Coor(BIRD_X, y, WIDTH_BIRD, HEIGH_BIRD, bird_image);
}


void Print_Score(uint16_t val, uint16_t x_score, uint16_t color) {
    char string[3] = {0, 0, '\0'};

    // Clear the previous score
    ILI9341_Fill_Color(x_score, Y_SCORE, x_score + 20, 239, YELLOW);

    if (val < 10) {
        //ILI9341_Draw_Char(char Character, uint8_t X, uint8_t Y, uint16_t Colour, uint16_t Size, uint16_t Background_Colour)
        ILI9341_Draw_Char((val + 48), x_score, Y_SCORE, RED, 2, YELLOW);
    } else {
        char a = val % 10 + 48;   // Units
        char b = val / 10 + 48;   // Tens
        string[0] = b;
        string[1] = a;
        //ILI9341_Draw_Text(const char* Text, uint8_t X, uint8_t Y, uint16_t Colour, uint16_t Size, uint16_t Background_Colour)
        ILI9341_Draw_Text(string, x_score, Y_SCORE, RED, 2, YELLOW);
    }
}


void Game_Over() {
    char score_string[3] = {0, 0, '\0'}, score_h_string[3] = {0,0,'\0'};
    uint16_t a = 0, b = 0, c = 0, d = 0;

      if(score > high_score){
              high_score = score;
      }
    // Clear the area for game over screen
    ILI9341_Fill_Color(X_GAME_OVER - 20, Y_GAME_OVER - 10, X_GAME_OVER + 130, Y_GAME_OVER + 110, RED);

    // Display "Game Over" text
    ILI9341_Draw_Text("Game Over", X_GAME_OVER, Y_GAME_OVER, YELLOW, 2, RED);

    ILI9341_Draw_Text("High Score:", X_GAME_H_SCORE, Y_GAME_H_SCORE, YELLOW, 2,RED);
    if (high_score < 10) {
        // Display single-digit score
        ILI9341_Draw_Char((high_score + 48), X_SCORE_H_END, Y_GAME_H_SCORE, BLUE, 2, RED);
    } else {
        // Display multi-digit score
        a = high_score % 10 + 48;    // Units
        b = high_score / 10 + 48;    // Tens
        score_h_string[0] = b;
        score_h_string[1] = a;
        ILI9341_Draw_Text(score_h_string, X_SCORE_H_END, Y_GAME_H_SCORE, BLUE, 2, RED);
    }
    // Display "Score: " text

    ILI9341_Draw_Text("Score: ", X_GAME_SCORE, Y_GAME_SCORE, YELLOW, 2, RED);

    if (score < 10) {
        // Display single-digit score
        ILI9341_Draw_Char((score + 48), X_SOCRE_END, Y_GAME_SCORE, BLUE, 2, RED);
    } else {
        // Display multi-digit score
        a = score % 10 + 48;    // Units
        b = score / 10 + 48;    // Tens
        score_string[0] = b;
        score_string[1] = a;
        ILI9341_Draw_Text(score_string, X_SOCRE_END, Y_GAME_SCORE, BLUE, 2, RED);
    }

    HAL_Delay(1500);

    // Display text play again
    ILI9341_Draw_Text("Play Again?", X_BUT, Y_BUT, WHITE, 2, BLACK);

    // You may need additional code to handle the delay and button press logic
}

void Init_Game() {
    Init_Heigh_Pill();
    score = 0;
    x1 = 320;
    x2 = 600;
    heigh_pill1 = list_heigh[rand() % 15];
    heigh_pill2 = 80;
    y_bird = BIRD_Y;
    x_com = 320;
    h_com = heigh_pill1;

    // Clear the screen
    ILI9341_Fill_Screen(WHITE);

    // Draw the bird image
    ILI9341_Write_Pic_Coor(BIRD_X, BIRD_Y, WIDTH_BIRD, HEIGH_BIRD, bird_image);

}

void Start_GameFlappy(){
	  int c = 0;
	  int score_old = 0;
	  int game_over=NO;

	  if (checkstartflappy == 0){
		  WelcomeFlappy();
		  checkstartflappy = 1;
      }

	if(!Read_IRQ()){

			  if((game_over==NO) || HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_1)== RESET){
			  	  score_old = score;
			  	  c = 0;
				  if(score_old > high_score){
				  		high_score = score_old;
				  }
				  Init_Game();
				  while(1){
						  if(x1 == 70){
							  x2 = 320;
							  heigh_pill2 = list_heigh[rand()%15];
						  }
						  if(x2 == 70){
							  x1 = 320;
							  heigh_pill1 = list_heigh[rand()%15];
						  }

						  Draw_Pillar(x1, heigh_pill1);
						  Draw_Pillar(x2, heigh_pill2);

						  if(!Read_IRQ()){
							  y_bird -= 5;
							  c = 1;
						  }
						  else if(c){
							  y_bird += 2;
						  }

						  if(x1 > 70){
							  x_com = x1;
							  h_com = heigh_pill1-1;
						  }
						  else{
							  x_com = x2;
							  h_com = heigh_pill2-1;
						  }
						  if(((x_com==X_COM)&&((y_bird<=h_com)||(y_bird+HEIGH_BIRD>=(h_com+DISTANCE))))||
							((y_bird<=h_com+1)&&( ((X_COM>=x_com)&&
							(X_COM <= (x_com+WIDTH_PILL)))||((BIRD_X>=x_com)&&(BIRD_X<=(x_com+WIDTH_PILL)))))||
							(((y_bird+HEIGH_BIRD)>=(h_com+DISTANCE))&&
							(((X_COM>=x_com)&&(X_COM <= (x_com+WIDTH_PILL)))||((BIRD_X>=x_com)&&
							(BIRD_X<=(x_com+WIDTH_PILL)))))||
							  ((y_bird+HEIGH_BIRD)>=HEIGH_SCREEN) || ((y_bird+HEIGH_BIRD)<=21)){

							  game_over = YES;
							  Game_Over();
							  break;
						  }

						  if(x1 == SCORED || x2 == SCORED){
							  score += 1;
						  }

						  if(c){
							  Bird_Fly(y_bird);
							  x1--;
							  x2--;
						  }
						  if (HAL_GPIO_ReadPin(GPIOE, GPIO_PIN_9) == GPIO_PIN_RESET) {
							  HAL_Delay(100); // รอสั�?ครู่เพื่อป้อง�?ัน�?าร�?ดซ้ำ
							  if (HAL_GPIO_ReadPin(GPIOE, GPIO_PIN_9) == GPIO_PIN_RESET) {
								  if (button_state == 0) {
									  button_state = 1;
									  // �?ารเปลี่ยนระดับ delay ตามค่า index ในอาร์เรย์
									  current_delay = delay_levels[delay_index];
									  delay_index = (delay_index + 1) % 3; // วนลูประหว่าง 0, 1, 2
								  }
							  }
						  } else {
							  button_state = 0;
						  }
						  HAL_Delay(current_delay); // ใช้ค่า delay ที่ถู�?เปลี่ยน�?ปลง

				  }
		  	  }
			}

}

/*-----------------------------------END FLAPPY BIRD-----------------------------------------------------------*/

/*------------------------------------PINGPONG-----------------------------------------------------------------*/

void WelcomePingpong(){
	 ILI9341_Set_Rotation(SCREEN_HORIZONTAL_2);
	 ILI9341_Fill_Screen(WHITE);
	 ILI9341_Draw_Text("PingPong Game",38, 40,BLACK,3,WHITE);

	 ILI9341_Draw_Filled_Circle(80, 180, 10, YELLOW);
	ILI9341_Draw_Text(":start game", 100, 170, BLACK, 2, WHITE);

	ILI9341_Draw_Filled_Circle(80, 210, 10, DARKGREEN);
	ILI9341_Draw_Text(":pause game", 100, 200, BLACK, 2, WHITE);
}

void StartGamePingpong(){
	if (checkstartpong == 0){
		WelcomePingpong();
		checkstartpong = 1;
	}

	if(HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_4) == GPIO_PIN_RESET){


		ILI9341_Fill_Screen(WHITE);
		reset_game = !reset_game;

		player_1_score = 0;
		player_2_score = 0;

		paddle_1_x1 = 60 ;
		paddle_1_x2 = 65 ;
		paddle_1_y1 = 78 ;
		paddle_1_y2 = 133;

		paddle_2_x1 = 240;
		paddle_2_x2 = 245;
		paddle_2_y1 = 78 ;
		paddle_2_y2 = 133;

		ball_x = 150;
		ball_y = 100;

		  // Toggle game_running
		  game_running = !game_running;
		  // Wait for button release
		  while (HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_3) == GPIO_PIN_RESET) {}
	  }
		// Check if button is pressed
		if (HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_3) == GPIO_PIN_RESET) {
			// Toggle game_running
			game_running = !game_running;
			// Wait for button release
		while (HAL_GPIO_ReadPin(GPIOD, GPIO_PIN_3) == GPIO_PIN_RESET) {}
		}

		// If game is running, call game function
		if (game_running) {
			PingPongGame();
		}
}
void PingPongGame(){
	  //DEBUG TERMINAL
	  adc_value = HAL_ADC_GetValue(&hadc1);
	  adc_value_2 = HAL_ADC_GetValue(&hadc2);
	  display(adc_value, adc_value_2);
//	  HAL_UART_Transmit(&huart3, (uint32_t*)&str, sizeof(str), 100);
//	  HAL_UART_Transmit(&huart3, (uint8_t*)str1, strlen(str1), 1000);
	  HAL_UART_Transmit(&huart3, (uint32_t*)str3, strlen(str3), 100);




		//check edge for paddle
		if(paddle_1_y1 <= 1){
			paddle_1_y1 = 1;
			paddle_1_y2 = 56;
		}else if (paddle_1_y2 >= 240){
			paddle_1_y1 = 185;
			paddle_1_y2 = 240;
		}if(paddle_2_y1 <= 1){
			paddle_2_y1 = 1;
			paddle_2_y2 = 56;
		}else if(paddle_2_y2 >= 240){
			paddle_2_y1 = 185;
			paddle_2_y2 = 240;
		}
	  	//Move Paddle
		if ( adc_value >= 0 && adc_value <= 2000) {
			// change paddle space
			if (paddle_1_y1 > 0) {
				paddle_1_y1--;
				paddle_1_y2--;
			}
		} else if (adc_value >= 2800 && adc_value <= 2890) {
			if (paddle_1_y2 < 240) {
				paddle_1_y1++;
				paddle_1_y2++;
			}
		}

		if (adc_value_2 >= 2800 && adc_value_2 <= 2890) {
			// change paddle space
			if (paddle_2_y1 > 0) {
				paddle_2_y1--;
				paddle_2_y2--;
			}
		} else if (adc_value_2 >= 0 && adc_value_2 <= 2000) {
			if (paddle_2_y2 < 240) {
				paddle_2_y1++;
				paddle_2_y2++;
			}
		}

		ILI9341_Draw_Filled_Rectangle_Coord(paddle_1_x1, paddle_1_y1, paddle_1_x2, paddle_1_y2, RED);
		ILI9341_Draw_Filled_Rectangle_Coord(oldpaddle_1_x1, oldpaddle_1_y1, oldpaddle_1_x2, oldpaddle_1_y2, WHITE);
		ILI9341_Draw_Filled_Rectangle_Coord(paddle_1_x1, paddle_1_y1, paddle_1_x2, paddle_1_y2, RED);

		oldpaddle_1_x1 = paddle_1_x1;
		oldpaddle_1_y1 = paddle_1_y1;
		oldpaddle_1_x2 = paddle_1_x2;
		oldpaddle_1_y2 = paddle_1_y2;

		//DRAW
		ILI9341_Draw_Filled_Rectangle_Coord(paddle_2_x1, paddle_2_y1, paddle_2_x2, paddle_2_y2, BLUE);
		ILI9341_Draw_Filled_Rectangle_Coord(oldpaddle_2_x1, oldpaddle_2_y1, oldpaddle_2_x2, oldpaddle_2_y2, WHITE);
		ILI9341_Draw_Filled_Rectangle_Coord(paddle_2_x1, paddle_2_y1, paddle_2_x2, paddle_2_y2, BLUE);

		oldpaddle_2_x1 = paddle_2_x1;
		oldpaddle_2_y1 = paddle_2_y1;
		oldpaddle_2_x2 = paddle_2_x2;
		oldpaddle_2_y2 = paddle_2_y2;

		 //UPDATE THE BALL
		if(game_running){
			move_ball();
		}



}



bool inPaddle(int x, int y, int rectX, int rectY, int rectWidth, int rectHeight) {
  bool  result = false;
  if ((x >= rectX && x <= rectWidth) &&
    (y >= rectY && y <= rectHeight)) {
    result = true;
  }
  return result;
}

void move_ball(){

	if(ball_x+2 == screen_hight || ball_x == 55){
		if(ball_x+2 == screen_hight){
			player_1_score += 1 ;
			HAL_GPIO_TogglePin(GPIOB, GPIO_PIN_11);

		}else if(ball_x == 55){
			player_2_score += 1;
			HAL_GPIO_TogglePin(GPIOB, GPIO_PIN_10);

		}
		//SEND BALL BACK TO SPAWN BALL AREA
		ball_x = 150;
		ball_y = 100;
		ball_color = BLACK;

		//MAKE IT MOVE DIFFERNT SIDE
		ballDirectionX = -ballDirectionX;
		ballDirectionY = -ballDirectionY;
	}


	// change ball space
	if (ball_y > screen_width || ball_y < 0) {
		    ballDirectionY = -ballDirectionY;
		}

	if (inPaddle(ball_x, ball_y, paddle_1_x1, paddle_1_y1, paddle_1_x2, paddle_1_y2)) {
		ballDirectionX = -ballDirectionX;

		ball_color = RED;


	}else if (inPaddle(ball_x, ball_y, paddle_2_x1, paddle_2_y1, paddle_2_x2, paddle_2_y2)){
		ballDirectionX = -ballDirectionX;
		ball_color = BLUE;
	}
		  ball_x += ballDirectionX;
		  ball_y += ballDirectionY;
		  ILI9341_Draw_Filled_Circle(ball_x, ball_y, 3, ball_color);
		  ILI9341_Draw_Filled_Circle(oldball_x, oldball_y, 3, WHITE);
		  ILI9341_Draw_Filled_Circle(ball_x, ball_y, 3, ball_color);

		  oldball_x = ball_x;
		  oldball_y = ball_y;
}

/*-----------------------------------------END PINGPONG-----------------------------------------*/

void delPaddle(){
	paddle_1_x1 = 0 ;
	paddle_1_x2 = 0 ;
	paddle_1_y1 = 0 ;
	paddle_1_y2 = 0;

	paddle_2_x1 = 0;
	paddle_2_x2 = 0;
	paddle_2_y1 = 0 ;
	paddle_2_y2 = 0;

	oldpaddle_1_x1 = paddle_1_x1;
	oldpaddle_1_y1 = paddle_1_y1;
	oldpaddle_1_x2 = paddle_1_x2;
	oldpaddle_1_y2 = paddle_1_y2;

	oldpaddle_2_x1 = paddle_2_x1;
	oldpaddle_2_y1 = paddle_2_y1;
	oldpaddle_2_x2 = paddle_2_x2;
	oldpaddle_2_y2 = paddle_2_y2;
}
//DISPLAY FUNCTION FOR DEBUG ON TERMINAL
void display(int val_1, int val_2){

	if(player_1_score == 5){

		game_running = false;
		delPaddle();

		ILI9341_Fill_Screen(BLACK);
		sprintf(str, "Player Score 1 : %d", player_1_score);
		ILI9341_Draw_Text(str, 30, 40, WHITE, 2,BLACK );

		sprintf(str, "Player Score 2 : %d", player_2_score);
		ILI9341_Draw_Text(str, 30, 80, WHITE, 2,BLACK );
		ILI9341_Draw_Text("Player 1 Wins!", 75, 130, WHITE, 2, BLACK);


	}
	else if(player_2_score == 5){


		game_running = false;
		delPaddle();

		ILI9341_Fill_Screen(BLACK);
		sprintf(str, "Player Score 1 : %d", player_1_score);
		ILI9341_Draw_Text(str, 30, 40, WHITE, 2,BLACK );

		sprintf(str, "Player Score 2 : %d", player_2_score);
		ILI9341_Draw_Text(str, 30, 80, WHITE, 2,BLACK );
		ILI9341_Draw_Text("Player 2 Wins!", 75, 130, WHITE, 2, BLACK);
	}
//	else{
//		sprintf(str, "Player Score 1 : %d Player Score 2 : %d", player_1_score, player_2_score);
//		ILI9341_Draw_Text(str, 20, 10, BLACK, 1, WHITE);
//	}

}




/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  while(1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
