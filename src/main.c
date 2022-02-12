/*
 *--------------------------------------
 * Program Name:
 * Author:
 * License:
 * Description:
 *--------------------------------------
*/

#include <string.h>

#include <tice.h>
#include <graphx.h>
#include <debug.h>
#include <keypadc.h>
#include <compression.h>
#include <fileioc.h>

static void PrintTime(float elapsed);
int findWord(const char * testword);
int objTest(void);
const char* testword1 = "QUIPU";    //1000th word in the list
const char* testword2 = "BAGGY";    //12971st word in the list (last word)
const char* testword3 = "AAAAA";    //word not in the dictionary

//perfcounter. Copied most of that stuff from the stopwatch example

int main(void)
{
    int i;
    int result;

    while (os_GetCSC());   //Wait until keys are released
    os_ClrHome();
    os_SetCursorPos(4, 4);

    result = objTest();
    if (result) {
        while (!os_GetCSC());
        return 1;
    }
    os_SetCursorPos(2, 2);
    os_PutStrFull("BEGIN MAIN TEST.");
    timer_Disable(1);
    timer_Set(1, 0);
    timer_Enable(1, TIMER_32K, TIMER_0INT, TIMER_UP);
    //Do programmy things.
    for(i=0; i<100; ++i) {
        result = findWord(testword3);

    }
    //End programmy things. Get the time.
    float elapsed = (float)timer_GetSafe(1, TIMER_UP) / 32768;
    PrintTime(elapsed);
    while (!os_GetCSC());
    return 0;
}
int objTest(void) {
    int result;
    real_t value;
    char str[16];

    result = findWord(testword1);
    value = os_FloatToReal((float)result);
    if (result != 1000) {
        os_SetCursorPos(3, 3);
        os_RealToStr(str, &value, 8, 1, 2);
        os_PutStrFull(str);
        os_SetCursorPos(4, 4);
        os_PutStrFull("TEST 1 FAIL.");
        return 1;
    }
    result = findWord(testword2);
    value = os_FloatToReal((float)result);
    if (result != 12971) {
        os_SetCursorPos(3, 3);
        os_RealToStr(str, &value, 8, 1, 2);
        os_PutStrFull(str);
        os_SetCursorPos(4, 4);
        os_PutStrFull("TEST 2 FAIL.");
        return 1;
    }
    result = findWord(testword3);
    value = os_FloatToReal((float)result);
    if (result != -1) {
        os_SetCursorPos(3, 3);
        os_RealToStr(str, &value, 8, 1, 2);
        os_PutStrFull(str);
        os_SetCursorPos(4, 4);
        os_PutStrFull("TEST 3 FAIL.");
        return 1;
    }
    return 0;
}


static void PrintTime(float elapsed)
{
    /* Float format for printf may be unimplemented, so go through an OS real */
    real_t elapsed_real;

    /* Max stopwatch value is (2^32 - 1) / 32768 = 131072.00, */
    /* so create a buffer with room for 9 characters plus a null terminator */
    char str[10];

    /* If the elapsed time is small enough that the OS would print it using */
    /* scientific notation, force it down to zero before conversion */
    elapsed_real = os_FloatToReal(elapsed <= 0.001f ? 0.0f : elapsed);

    /* Convert the elapsed time real to a string */
    os_RealToStr(str, &elapsed_real, 8, 1, 2);

    /* print the string */
    os_SetCursorPos(4, 4);
    os_PutStrFull(str);
}


