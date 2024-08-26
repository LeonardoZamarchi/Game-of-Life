import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

def calcular_entropia(probabilidades):
    probabilidades = np.array(probabilidades)
    return -np.sum(probabilidades * np.log2(probabilidades + 1e-9))

def game_of_life_step(grid):
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1)
                    for i in (-1, 0, 1) for j in (-1, 0, 1)
                    if (i != 0 or j != 0))
    return (neighbors == 3) | (grid & (neighbors == 2))

def calcular_entropia_jogo(grid):
    prob_vivo = np.mean(grid)
    prob_morto = 1 - prob_vivo
    return calcular_entropia([prob_vivo, prob_morto])

# Configuração inicial com percentual de células vivas baseado no slider
initial_prob_vivo = 0.5
grid = np.random.choice([0, 1], size=(10, 10), p=[1-initial_prob_vivo, initial_prob_vivo])

# Configurar a figura para a animação
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)
im = ax.imshow(grid, cmap='binary', vmin=0, vmax=1)

# Cria o eixo do slider
axcolor = 'lightgoldenrodyellow'
ax_prob = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
slider_prob = Slider(ax_prob, 'Prob Vivos', 0, 1, valinit=initial_prob_vivo)

# Slider para controlar a velocidade da simulação
ax_speed = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider_speed = Slider(ax_speed, 'Velocidade', 10, 1000, valinit=100, valstep=10)

# Adicionar botões de Play, Pause e Reset
ax_play = plt.axes([0.25, 0.05, 0.1, 0.04])
ax_pause = plt.axes([0.35, 0.05, 0.1, 0.04])
ax_reset = plt.axes([0.45, 0.05, 0.1, 0.04])

button_play = Button(ax_play, 'Play')
button_pause = Button(ax_pause, 'Pause')
button_reset = Button(ax_reset, 'Reset')

entropias = []
is_paused = False
ani = None  # Placeholder for animation object

def update(frame):
    global grid, is_paused
    if not is_paused:
        grid = game_of_life_step(grid)
        entropia = calcular_entropia_jogo(grid)
        entropias.append(entropia)
        im.set_data(grid)
    return [im]

def update_slider(val):
    global grid
    prob_vivo = slider_prob.val
    grid = np.random.choice([0, 1], size=(10, 10), p=[1-prob_vivo, prob_vivo])
    im.set_data(grid)

def update_speed(val):
    global ani
    ani.event_source.interval = slider_speed.val  # Update the animation speed

def play(event):
    global is_paused
    is_paused = False

def pause(event):
    global is_paused
    is_paused = True

def reset(event):
    global grid, entropias
    prob_vivo = slider_prob.val
    grid = np.random.choice([0, 1], size=(10, 10), p=[1-prob_vivo, prob_vivo])
    entropias.clear()
    im.set_data(grid)
    plt.draw()

slider_prob.on_changed(update_slider)
slider_speed.on_changed(update_speed)
button_play.on_clicked(play)
button_pause.on_clicked(pause)
button_reset.on_clicked(reset)

# Configurar e iniciar a animação
ani = animation.FuncAnimation(fig, update, frames=100, interval=slider_speed.val, blit=True)

plt.show()

# Mostrar a entropia ao longo do tempo
plt.figure()
plt.plot(entropias)
plt.xlabel('Iteração')
plt.ylabel('Entropia')
plt.title('Entropia no Jogo da Vida')
plt.show()
