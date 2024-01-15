from flask import Flask, render_template, request, url_for, redirect, session, flash
import os

app=Flask("monapp")

@app.route("/")
def index():
  return render_template("index.html")

app.run("0.0.0.0", port=81)