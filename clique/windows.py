import tkinter as tk	
from tkinter import *
from tkinter import DISABLED, END, INSERT, filedialog

####################   ADVANCED SEGMENTATION OPTIONS WINDOW   ####################

advanced_segmentation_options = {'epsilon_input' : 0.85, 'kmeans_iterations' : 100, 'kmeans_attempts' : 10}

#function to update advances segmentation clustering options
def save_advanced_segmentation_options(advanced_segmentation_options):
    #check that epsilon is valid
    try:
        epsilon_value = float(epsilon_input.get())
        advanced_segmentation_options['epsilon_input'] = epsilon_value
    except:
        tk.messagebox.showerror("Input Error", f"Error: {epsilon_input.get()} is an invalid epsilon value.")
    
    #check that iterations is valid
    try:
        kmeans_iterations = int(kmeans_iterations_input.get())
        advanced_segmentation_options['kmeans_iterations'] = kmeans_iterations
    except:
        tk.messagebox.showerror("Input Error", f"Error: {kmeans_iterations_input.get()} is an invalid iterations value.")

    try:
        kmeans_attempts = int(kmeans_iterations_input.get())
        advanced_segmentation_options['kmeans_attempts'] = kmeans_attempts
    except:
        tk.messagebox.showerror("Input Error", f"Error: {kmeans_iterations_input.get()} is an attempts iterations value.")

def advanced_segmentation_window(parent, advanced_segmentation_options):
    window = Toplevel(parent)
    window.title("Advanced Color Segmentation Options")
    window.geometry('325x400')

    #ADVANCED K-MEANS CLUSTERING LABELED FRAME
    advancedKmeansFrame = tk.LabelFrame(window, text="K-means clustering advanced options")
    advancedKmeansFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to specify epsilon
    epsilonPrompt = tk.Label(advancedKmeansFrame, text="Epsilon:")
    epsilonPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for epsilon
    global epsilon_input
    epsilon_input = tk.Entry(advancedKmeansFrame)
    epsilon_input.grid(row=1, column=2, padx=10, pady=5)
    #set default
    epsilon_input.insert(0, '0.85')
    #update entry
    if 'epsilon_input' in advanced_segmentation_options:
        epsilon_input.delete(0, END)   
        epsilon_input.insert(0, f"{advanced_segmentation_options['epsilon_input']}")

    #add prompt to specify iterations
    iterationsPrompt = tk.Label(advancedKmeansFrame, text="Iterations:")
    iterationsPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for iterations
    global kmeans_iterations_input
    kmeans_iterations_input = tk.Entry(advancedKmeansFrame)
    kmeans_iterations_input.grid(row=2, column=2, padx=10, pady=5)
    #set default
    kmeans_iterations_input.insert(0, '100')
    #update entry
    if 'kmeans_iterations' in advanced_segmentation_options:
        kmeans_iterations_input.delete(0, END)   
        kmeans_iterations_input.insert(0, f"{advanced_segmentation_options['kmeans_iterations']}")

    #add prompt to specify attempts
    kmeansAttemptsPrompt = tk.Label(advancedKmeansFrame, text="Attempts:")
    kmeansAttemptsPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for attempts
    global kmeans_attempts_input
    kmeans_attempts_input = tk.Entry(advancedKmeansFrame)
    kmeans_attempts_input.grid(row=3, column=2, padx=10, pady=5)
    #set default
    kmeans_attempts_input.insert(0, '10')
    #update entry
    if 'kmeans_attempts' in advanced_segmentation_options:
        kmeans_attempts_input.delete(0, END)   
        kmeans_attempts_input.insert(0, f"{advanced_segmentation_options['kmeans_attempts']}")

    #add button to export information back to main window
    exportOptionsButton = tk.Button(window, text="Save", command=lambda: save_advanced_segmentation_options(advanced_segmentation_options))
    exportOptionsButton.grid(row=2, column=0, sticky = "ew", pady=5, padx=10)