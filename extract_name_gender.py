import requests
from tqdm import tqdm
if __name__ == '__main__':
    start = 1
    # Each member url start with his member_id
    for member in tqdm(range(start, 1500000)):
        r = requests.get(f'https://www.fxp.co.il/member.php?u={member}')
        try:
            # Get the text from the response
            t = r.text
            # Get the start location of the user_name
            start_index = t.index('<li class="navbit lastnavbit"><span>') + 36
            end_index = t[start_index:].index('</span>') + start_index
            user_name = t[start_index:end_index]
            # Get the gender of the user if present
            gender = 'm' if '<dt>מין:</dt>\n<dd>זכר' in t else 'f' if '<dt>מין:</dt>\n<dd>נקבה' in t else None
            if gender is not None:
                # Write it to fxp_users.txt as a new line
                # member_id user_name   gender
                with open('fxp_user.txt', 'a') as f:
                    f.write(f'{member}\t{user_name}\t{gender}\n')
        # If an error occurred save it to error.txt
        except Exception as e:
            with open('error.txt', 'a') as f:
                f.write(f'{member}\t{e}\n')
