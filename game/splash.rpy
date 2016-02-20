init python:
    if persistent.disclaimer_seen is None:
        persistent.disclaimer_seen = False

init:
    image disclaimer:
        Text(_("""\n{color=#fff}{size=80}Disclaimer{/size}\n{size=25}This game contains mild cartoon violence and strong language. Additionally it contains slightly mad and overly attached cubes. Player discretion is advised.\nThis is a school project with the purpose of repeating everything we've learned so far in the subject Communication/IT. We've tried to include as much as possible, however, the game would be way to long if we were to repeat everything we've been through. This project has been released under an MIT license at {a=https://github.com/bomjacob/repetition}github.com/bomjacob/repetition{/a}{vspace=215}{size=20}
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.{/size}
{/color}"""), text_align=0.5, xmaximum=900)
    image ctc:
        linear 0.75 alpha 1.0
        Text(_("""{color=#fff}{size=20}Press any key to continue{/size}{/color}\n"""), text_align=0.5, xmaximum=740)
        linear 0.75 alpha 0.25
        repeat

label splashscreen:
    scene black

    $ renpy.music.play("KK--Love-Song", loop=True, fadein=1)

    $ renpy.pause(0.5)

    show disclaimer at top with dissolve
    if not persistent.disclaimer_seen:
        $ renpy.pause(5.0, hard=True)
        show ctc at center with dissolve
        $ renpy.pause()
    else:
        show ctc at center with dissolve
        $ renpy.pause(5)
    hide disclaimer
    hide ctc
    with dissolve
    $ persistent.disclaimer_seen = True

    show text _("{color=#fff}{size=+40}Neko Productions {/size}{image=ui/neko.png}\n{size=+10}presents...{/size}{/color}") at truecenter with dissolve
    $ renpy.pause(2, hard=False)

    hide text with dissolve
    $ renpy.pause(0.5, hard=False)

    return