from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/a')
def audioCtl():
  os.system("""osascript -l JavaScript -e \"
    const chrome = Application('Google Chrome');
    chrome.windows().forEach((window, windowIndex) => {
      const tabIndex = window.tabs().findIndex(tab => tab.url().startsWith('https://meet.google.com/'));
      if (tabIndex >= 0) {
        chrome.activate();
        window.activeTabIndex = tabIndex + 1;
        const se = Application('System Events');
        se.processes['Google Chrome'].windows[windowIndex].actions['AXRaise'].perform();
        delay(0.1);
        se.keystroke('d', { using: ['command down']});
      }
    });
  \"""")
  return render_template('index.html')

@app.route('/v')
def videoCtl():
  os.system("""osascript -l JavaScript -e \"
    const chrome = Application('Google Chrome');
    chrome.windows().forEach((window, windowIndex) => {
      const tabIndex = window.tabs().findIndex(tab => tab.url().startsWith('https://meet.google.com/'));
      if (tabIndex >= 0) {
        chrome.activate();
        window.activeTabIndex = tabIndex + 1;
        const se = Application('System Events');
        se.processes['Google Chrome'].windows[windowIndex].actions['AXRaise'].perform();
        delay(0.1);
        se.keystroke('e', { using: ['command down']});
      }
    });
  \"""")
  return render_template('index.html')

@app.route('/z')
def zoomActivate():
  os.system("""osascript -l JavaScript -e \"
    const chrome = Application('Google Chrome');
    chrome.windows().forEach((window, windowIndex) => {
      const tabIndex = window.tabs().findIndex(tab => tab.url().startsWith('https://meet.google.com/'));
      if (tabIndex >= 0) {
        chrome.activate();
        window.activeTabIndex = tabIndex + 1;
        const se = Application('System Events');
        se.processes['Google Chrome'].windows[windowIndex].actions['AXRaise'].perform();
      }
    });
  \"""")
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
