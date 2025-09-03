# NationalAnthem/Lyrics.py

from colorama import init, Fore, Style
import time
import os

# Initialize colorama for colored text (works on Windows too)
init()

# Lyrics of the Philippine National Anthem
lyrics = """
Bayang Magiliw, Perlas ng Silanganan
Alab ng Puso sa dibdib mo'y buhay
Lupang Hinirang, Duyan ka ng magiting,
Sa manlulupig di ka pasisiil.

Sa dagat at bundok,
Sa simoy at sa langit mong bughaw,
May dilag ang tula at awit
Sa paglayang minamahal.

Ang kislap ng watawat mo'y
Tagumapay na nagniningning 
Ang bituin at araw niya
Kailan pa ma'y di magdidilim 

Lupa ng araw, ng luwalhati't pagsinta
Buhay ay langit sa piling mo
Aming ligaya na 'pag may mang-aapi
Ang mamatay ng dahil sa 'yo
"""

def display_lyrics():
    # Clear the console for a clean display
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Header with ASCII art
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print("🎵 Philippine National Anthem: Lupang Hinirang 🎵")
    print("=" * 50 + Style.RESET_ALL)
    
    # Split lyrics into stanzas and display with delay for effect
    stanzas = lyrics.strip().split('\n\n')
    for stanza in stanzas:
        print(Fore.YELLOW + stanza + Style.RESET_ALL)
        print()  # Space between stanzas
        time.sleep(2)  # Pause for readability
    
    print(Fore.CYAN + "=" * 50)
    print("End of Lyrics" + Style.RESET_ALL)

if __name__ == "__main__":
    display_lyrics()