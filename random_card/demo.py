"""Run the card simulation."""

from random_card import CardSimulator

if __name__ == '__main__':
    card_simulation = CardSimulator()
    sim_iterations = card_simulation.iterations
    sim_input = 'How many simulations [%s]?' % (sim_iterations)
    iterations = input(sim_input) or sim_iterations
    show_graph_input = input('Want to see a graph y/n [y]?') or 'y'
    show_graph = True
    if (show_graph_input == 'n' or show_graph_input == 'N'):
        show_graph = False

    card_simulation.set_iterations(iterations)
    card_simulation.set_trials()
    card_simulation.print_stats()
    if (show_graph is True):
        card_simulation.render_graph()
