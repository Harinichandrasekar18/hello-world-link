from flask import Flask
app=Flask('__name__')
@app.route('/')
def Dad():
    return "<center><h1>Dad</h1></center><br><p>Dad refers to the male parent of a child in a family. He is a very important member of the family. He is the one who takes care of the entire family including his own parents, wife and children. He earns his bread and butter for his family and tries his best to fulfil their needs and demands.</p></body>"

@app.route('/family')
def mother():
    return "<center><h1>MoM</h1></center><br><p>First of all, Mother is a word which fills everyone with emotions. A Mother is certainly the most important human being in everyone’s life. Mother’s Love for her child certainly cannot be compared with anything. Her level of forgiveness is unmatchable. A Mother is capable of forgiving any wrongdoing. Mother is the most important woman in everyone’s life. A mother sacrifices her happiness for her child. No one else can care for their kids the way a Mother does.  A Mother is great and does not need anyone like me explaining that. This essay on Mother is a small attempt to discover the greatness of a mother.</p>"

if __name__=="__main__":
    app.run(debug=True)
