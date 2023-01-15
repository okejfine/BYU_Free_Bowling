# Alex King
# Function to define process to check if valid ID. Better version would use an API call, or have some sort of pre-check
# to make sure it is a valid BYU ID card.
# Maybe the card swipe shows something to validate the card. This will do for now.
card_id = input("Enter a card ID: ")

def is_valid_id(card_id):
    if len(card_id) != 9:
        return False
    if not card_id.isnumeric():
        return False
    return True
# check for valid ID, record new valid ID, reject non-valid
with open("used_ids.txt", mode='r') as infile:
    content = infile.read()
    # reject not valid ID
    if not is_valid_id(card_id):
        print("Sorry, not a valid ID.")
    # reject already used id
    if card_id in (content):
        print("Sorry, this ID has used it's free game.")
    # record and accept new valid id
    if is_valid_id(card_id) and card_id not in (content):
        with open('used_ids.txt', mode="a") as f:
            f.write(f"{card_id}\n")
        print("Your free game has been recorded for this semester. Enjoy!")
print("Go Cougs!")
