import random
import string

def alpha_num_random(length:int,/,*,letters:bool=True,punc:bool=True,digit:bool=True,duplicated:bool=False)->str:

    """
        Generate a random alphanumeric string with optional letters, digits, and punctuation.

        Parameters
        ----------
        length : int (positional-only)
            The length of the output string.
        
        letters : bool, optional (default=True)
            If True, include uppercase and lowercase letters in the output string.
        
        punc : bool, optional (default=True)
            If True, include punctuation characters in the output string.
        
        digit : bool, optional (default=True)
            If True, include numeric digits in the output string.
        
        duplicated : bool, optional (default=False)
            If True, allow duplicate characters in the output string.
            If False, each character in the output string will be unique.

        Returns
        -------
        str
            A random string of the specified length, based on the given options.
            Returns None if an error occurs (e.g., length > available characters when `duplicated=False`).

        Examples
        --------
        >>> alpha_num_random(10)
        'aD7&hQmP0!'
        
        >>> alpha_num_random(8, letters=True, punc=False, digit=True)
        'h7kD2aXz'

        >>> alpha_num_random(6, letters=True, punc=True, digit=False, duplicated=True)
        '%aZ&@%'

        >>> alpha_num_random(5, letters=False, punc=False, digit=True)
        '73910'

        Notes
        -----
        - `length` must not exceed the total available characters if `duplicated=False`.
        For example, if `letters=False, punc=False, digit=True`, then `length` cannot exceed 10 (the number of digits).
    """

    try :
        a=""
        p=al=d=[]

        al=[i for i in string.ascii_letters] if letters else al
        p=[i for i in string.punctuation] if punc else p
        d=[i for i in string.digits] if digit else d

        final_list=p+al+d
        random.shuffle(final_list)
    
        if duplicated:
            ran_list=random.choices(final_list,k=length)
            ran_str=[a:=a+i for i in ran_list]
        else:
            ran_list=random.sample(final_list,length)
            ran_str=[a:=a+i for i in ran_list]

        return ran_str[-1]
    
    except:
        return None
    
if __name__=="__main__":
    st=alpha_num_random(10)
    print(st)