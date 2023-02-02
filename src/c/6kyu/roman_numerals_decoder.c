int char_to_int(char c)
{
    switch (c)
    {
    case 'I':
        return 1;
    case 'V':
        return 5;
    case 'X':
        return 10;
    case 'L':
        return 50;
    case 'C':
        return 100;
    case 'D':
        return 500;
    case 'M':
        return 1000;
    default:
        return 0;
    }
}

unsigned decode_roman(const char *roman_number)
{
    int result = 0;
    int last = 0;
    int var;
    unsigned int lenght = 0;

    while (roman_number[lenght]) lenght++;
    for (unsigned int i = lenght; i > 0; i--) {
        var = char_to_int(roman_number[i - 1]);
        result += (var >= last) ? var : -var;
        last = var;
    }
  	return result;
}
