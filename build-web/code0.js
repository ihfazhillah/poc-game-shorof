gdjs.MenuCode = {};
gdjs.MenuCode.localVariables = [];
gdjs.MenuCode.idToCallbackMap = new Map();
gdjs.MenuCode.forEachIndex2 = 0;

gdjs.MenuCode.forEachObjects2 = [];

gdjs.MenuCode.forEachTemporary2 = null;

gdjs.MenuCode.forEachTotalCount2 = 0;

gdjs.MenuCode.GDJudulObjects1= [];
gdjs.MenuCode.GDJudulObjects2= [];
gdjs.MenuCode.GDJudulObjects3= [];
gdjs.MenuCode.GDSubJudulObjects1= [];
gdjs.MenuCode.GDSubJudulObjects2= [];
gdjs.MenuCode.GDSubJudulObjects3= [];
gdjs.MenuCode.GDTombolBabObjects1= [];
gdjs.MenuCode.GDTombolBabObjects2= [];
gdjs.MenuCode.GDTombolBabObjects3= [];
gdjs.MenuCode.GDLabelBabObjects1= [];
gdjs.MenuCode.GDLabelBabObjects2= [];
gdjs.MenuCode.GDLabelBabObjects3= [];
gdjs.MenuCode.GDTombolRakObjects1= [];
gdjs.MenuCode.GDTombolRakObjects2= [];
gdjs.MenuCode.GDTombolRakObjects3= [];
gdjs.MenuCode.GDPetunjukObjects1= [];
gdjs.MenuCode.GDPetunjukObjects2= [];
gdjs.MenuCode.GDPetunjukObjects3= [];
gdjs.MenuCode.GDPetualangObjects1= [];
gdjs.MenuCode.GDPetualangObjects2= [];
gdjs.MenuCode.GDPetualangObjects3= [];
gdjs.MenuCode.GDKepalaPetualangObjects1= [];
gdjs.MenuCode.GDKepalaPetualangObjects2= [];
gdjs.MenuCode.GDKepalaPetualangObjects3= [];
gdjs.MenuCode.GDKelinciObjects1= [];
gdjs.MenuCode.GDKelinciObjects2= [];
gdjs.MenuCode.GDKelinciObjects3= [];
gdjs.MenuCode.GDKepalaKelinciObjects1= [];
gdjs.MenuCode.GDKepalaKelinciObjects2= [];
gdjs.MenuCode.GDKepalaKelinciObjects3= [];
gdjs.MenuCode.GDTelurObjects1= [];
gdjs.MenuCode.GDTelurObjects2= [];
gdjs.MenuCode.GDTelurObjects3= [];
gdjs.MenuCode.GDTelurTerbangObjects1= [];
gdjs.MenuCode.GDTelurTerbangObjects2= [];
gdjs.MenuCode.GDTelurTerbangObjects3= [];
gdjs.MenuCode.GDKeranjangObjects1= [];
gdjs.MenuCode.GDKeranjangObjects2= [];
gdjs.MenuCode.GDKeranjangObjects3= [];
gdjs.MenuCode.GDRumputObjects1= [];
gdjs.MenuCode.GDRumputObjects2= [];
gdjs.MenuCode.GDRumputObjects3= [];
gdjs.MenuCode.GDPohonObjects1= [];
gdjs.MenuCode.GDPohonObjects2= [];
gdjs.MenuCode.GDPohonObjects3= [];
gdjs.MenuCode.GDSemakObjects1= [];
gdjs.MenuCode.GDSemakObjects2= [];
gdjs.MenuCode.GDSemakObjects3= [];
gdjs.MenuCode.GDBungaObjects1= [];
gdjs.MenuCode.GDBungaObjects2= [];
gdjs.MenuCode.GDBungaObjects3= [];
gdjs.MenuCode.GDBatuObjects1= [];
gdjs.MenuCode.GDBatuObjects2= [];
gdjs.MenuCode.GDBatuObjects3= [];
gdjs.MenuCode.GDAsapObjects1= [];
gdjs.MenuCode.GDAsapObjects2= [];
gdjs.MenuCode.GDAsapObjects3= [];
gdjs.MenuCode.GDTandaStartObjects1= [];
gdjs.MenuCode.GDTandaStartObjects2= [];
gdjs.MenuCode.GDTandaStartObjects3= [];
gdjs.MenuCode.GDPanelPetaObjects1= [];
gdjs.MenuCode.GDPanelPetaObjects2= [];
gdjs.MenuCode.GDPanelPetaObjects3= [];
gdjs.MenuCode.GDPetaSelObjects1= [];
gdjs.MenuCode.GDPetaSelObjects2= [];
gdjs.MenuCode.GDPetaSelObjects3= [];
gdjs.MenuCode.GDPetaTelurObjects1= [];
gdjs.MenuCode.GDPetaTelurObjects2= [];
gdjs.MenuCode.GDPetaTelurObjects3= [];
gdjs.MenuCode.GDPetaPemainObjects1= [];
gdjs.MenuCode.GDPetaPemainObjects2= [];
gdjs.MenuCode.GDPetaPemainObjects3= [];
gdjs.MenuCode.GDPetaStartObjects1= [];
gdjs.MenuCode.GDPetaStartObjects2= [];
gdjs.MenuCode.GDPetaStartObjects3= [];
gdjs.MenuCode.GDPetaFinishObjects1= [];
gdjs.MenuCode.GDPetaFinishObjects2= [];
gdjs.MenuCode.GDPetaFinishObjects3= [];
gdjs.MenuCode.GDTandaFinishObjects1= [];
gdjs.MenuCode.GDTandaFinishObjects2= [];
gdjs.MenuCode.GDTandaFinishObjects3= [];
gdjs.MenuCode.GDPanahObjects1= [];
gdjs.MenuCode.GDPanahObjects2= [];
gdjs.MenuCode.GDPanahObjects3= [];
gdjs.MenuCode.GDBonekaObjects1= [];
gdjs.MenuCode.GDBonekaObjects2= [];
gdjs.MenuCode.GDBonekaObjects3= [];


gdjs.MenuCode.eventsList0 = function(runtimeScene) {

};gdjs.MenuCode.eventsList1 = function(runtimeScene) {

{


let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.runtimeScene.sceneJustBegins(runtimeScene);
if (isConditionTrue_0) {
gdjs.copyArray(runtimeScene.getObjects("KepalaKelinci"), gdjs.MenuCode.GDKepalaKelinciObjects2);
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/suara/pilih_wazan.mp3", false, 100, 1);
}
{for(var i = 0, len = gdjs.MenuCode.GDKepalaKelinciObjects2.length ;i < len;++i) {
    gdjs.MenuCode.GDKepalaKelinciObjects2[i].getBehavior("Animation").setAnimationName("biasa");
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("LabelBab"), gdjs.MenuCode.GDLabelBabObjects1);

for (gdjs.MenuCode.forEachIndex2 = 0;gdjs.MenuCode.forEachIndex2 < gdjs.MenuCode.GDLabelBabObjects1.length;++gdjs.MenuCode.forEachIndex2) {
gdjs.MenuCode.GDLabelBabObjects2.length = 0;


gdjs.MenuCode.forEachTemporary2 = gdjs.MenuCode.GDLabelBabObjects1[gdjs.MenuCode.forEachIndex2];
gdjs.MenuCode.GDLabelBabObjects2.push(gdjs.MenuCode.forEachTemporary2);
let isConditionTrue_0 = false;
if (true) {
{for(var i = 0, len = gdjs.MenuCode.GDLabelBabObjects2.length ;i < len;++i) {
    gdjs.MenuCode.GDLabelBabObjects2[i].getBehavior("Text").setText(runtimeScene.getGame().getVariables().getFromIndex(3).getChild(gdjs.MenuCode.GDLabelBabObjects2[i].getVariables().getFromIndex(0).getAsNumber() - 1).getAsString());
}
}
{for(var i = 0, len = gdjs.MenuCode.GDLabelBabObjects2.length ;i < len;++i) {
    gdjs.MenuCode.GDLabelBabObjects2[i].setPadding(25);
}
}
}
}

}


};gdjs.MenuCode.eventsList2 = function(runtimeScene) {

{


let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.runtimeScene.sceneJustBegins(runtimeScene);
if (isConditionTrue_0) {
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.storage.elementExistsInJSONFile("TelurWazan", "koleksi");
}
if (isConditionTrue_0) {
{gdjs.evtTools.storage.readStringFromJSONFile("TelurWazan", "koleksi", runtimeScene, runtimeScene.getScene().getVariables().getFromIndex(0));
}
{gdjs.evtTools.network.jsonToVariableStructure(runtimeScene.getScene().getVariables().getFromIndex(0).getAsString(), runtimeScene.getGame().getVariables().getFromIndex(4));
}
}

}


};gdjs.MenuCode.eventsList3 = function(runtimeScene) {

{


let isConditionTrue_0 = false;
{
gdjs.copyArray(runtimeScene.getObjects("Kelinci"), gdjs.MenuCode.GDKelinciObjects1);
gdjs.copyArray(runtimeScene.getObjects("KepalaKelinci"), gdjs.MenuCode.GDKepalaKelinciObjects1);
gdjs.copyArray(runtimeScene.getObjects("KepalaPetualang"), gdjs.MenuCode.GDKepalaPetualangObjects1);
gdjs.copyArray(runtimeScene.getObjects("Petualang"), gdjs.MenuCode.GDPetualangObjects1);
{for(var i = 0, len = gdjs.MenuCode.GDKepalaPetualangObjects1.length ;i < len;++i) {
    gdjs.MenuCode.GDKepalaPetualangObjects1[i].setX((( gdjs.MenuCode.GDPetualangObjects1.length === 0 ) ? 0 :gdjs.MenuCode.GDPetualangObjects1[0].getPointX("")) + 4);
}
}
{for(var i = 0, len = gdjs.MenuCode.GDKepalaPetualangObjects1.length ;i < len;++i) {
    gdjs.MenuCode.GDKepalaPetualangObjects1[i].setY((( gdjs.MenuCode.GDPetualangObjects1.length === 0 ) ? 0 :gdjs.MenuCode.GDPetualangObjects1[0].getPointY("")) - 50);
}
}
{for(var i = 0, len = gdjs.MenuCode.GDKepalaKelinciObjects1.length ;i < len;++i) {
    gdjs.MenuCode.GDKepalaKelinciObjects1[i].setX((( gdjs.MenuCode.GDKelinciObjects1.length === 0 ) ? 0 :gdjs.MenuCode.GDKelinciObjects1[0].getPointX("")) - 4);
}
}
{for(var i = 0, len = gdjs.MenuCode.GDKepalaKelinciObjects1.length ;i < len;++i) {
    gdjs.MenuCode.GDKepalaKelinciObjects1[i].setY((( gdjs.MenuCode.GDKelinciObjects1.length === 0 ) ? 0 :gdjs.MenuCode.GDKelinciObjects1[0].getPointY("")) - 62);
}
}
}

}


};gdjs.MenuCode.mapOfGDgdjs_9546MenuCode_9546GDTombolBabObjects2Objects = Hashtable.newFrom({"TombolBab": gdjs.MenuCode.GDTombolBabObjects2});
gdjs.MenuCode.mapOfGDgdjs_9546MenuCode_9546GDTombolRakObjects1Objects = Hashtable.newFrom({"TombolRak": gdjs.MenuCode.GDTombolRakObjects1});
gdjs.MenuCode.eventsList4 = function(runtimeScene) {

{

gdjs.copyArray(runtimeScene.getObjects("TombolBab"), gdjs.MenuCode.GDTombolBabObjects2);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.cursorOnObject(gdjs.MenuCode.mapOfGDgdjs_9546MenuCode_9546GDTombolBabObjects2Objects, runtimeScene, true, false);
if (isConditionTrue_0) {
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.isMouseButtonReleased(runtimeScene, "Left");
}
if (isConditionTrue_0) {
/* Reuse gdjs.MenuCode.GDTombolBabObjects2 */
{runtimeScene.getGame().getVariables().getFromIndex(2).setNumber(((gdjs.MenuCode.GDTombolBabObjects2.length === 0 ) ? gdjs.VariablesContainer.badVariablesContainer : gdjs.MenuCode.GDTombolBabObjects2[0].getVariables()).getFromIndex(0).getAsNumber());
}
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/sfx/klik.wav", false, 100, 1);
}
{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Hutan", false);
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("TombolRak"), gdjs.MenuCode.GDTombolRakObjects1);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.cursorOnObject(gdjs.MenuCode.mapOfGDgdjs_9546MenuCode_9546GDTombolRakObjects1Objects, runtimeScene, true, false);
if (isConditionTrue_0) {
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.isMouseButtonReleased(runtimeScene, "Left");
}
if (isConditionTrue_0) {
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/sfx/klik.wav", false, 100, 1);
}
{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Koleksi", false);
}
}

}


};gdjs.MenuCode.eventsList5 = function(runtimeScene) {

{


gdjs.MenuCode.eventsList1(runtimeScene);
}


{


gdjs.MenuCode.eventsList2(runtimeScene);
}


{


gdjs.MenuCode.eventsList3(runtimeScene);
}


{


gdjs.MenuCode.eventsList4(runtimeScene);
}


};

gdjs.MenuCode.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();

gdjs.MenuCode.GDJudulObjects1.length = 0;
gdjs.MenuCode.GDJudulObjects2.length = 0;
gdjs.MenuCode.GDJudulObjects3.length = 0;
gdjs.MenuCode.GDSubJudulObjects1.length = 0;
gdjs.MenuCode.GDSubJudulObjects2.length = 0;
gdjs.MenuCode.GDSubJudulObjects3.length = 0;
gdjs.MenuCode.GDTombolBabObjects1.length = 0;
gdjs.MenuCode.GDTombolBabObjects2.length = 0;
gdjs.MenuCode.GDTombolBabObjects3.length = 0;
gdjs.MenuCode.GDLabelBabObjects1.length = 0;
gdjs.MenuCode.GDLabelBabObjects2.length = 0;
gdjs.MenuCode.GDLabelBabObjects3.length = 0;
gdjs.MenuCode.GDTombolRakObjects1.length = 0;
gdjs.MenuCode.GDTombolRakObjects2.length = 0;
gdjs.MenuCode.GDTombolRakObjects3.length = 0;
gdjs.MenuCode.GDPetunjukObjects1.length = 0;
gdjs.MenuCode.GDPetunjukObjects2.length = 0;
gdjs.MenuCode.GDPetunjukObjects3.length = 0;
gdjs.MenuCode.GDPetualangObjects1.length = 0;
gdjs.MenuCode.GDPetualangObjects2.length = 0;
gdjs.MenuCode.GDPetualangObjects3.length = 0;
gdjs.MenuCode.GDKepalaPetualangObjects1.length = 0;
gdjs.MenuCode.GDKepalaPetualangObjects2.length = 0;
gdjs.MenuCode.GDKepalaPetualangObjects3.length = 0;
gdjs.MenuCode.GDKelinciObjects1.length = 0;
gdjs.MenuCode.GDKelinciObjects2.length = 0;
gdjs.MenuCode.GDKelinciObjects3.length = 0;
gdjs.MenuCode.GDKepalaKelinciObjects1.length = 0;
gdjs.MenuCode.GDKepalaKelinciObjects2.length = 0;
gdjs.MenuCode.GDKepalaKelinciObjects3.length = 0;
gdjs.MenuCode.GDTelurObjects1.length = 0;
gdjs.MenuCode.GDTelurObjects2.length = 0;
gdjs.MenuCode.GDTelurObjects3.length = 0;
gdjs.MenuCode.GDTelurTerbangObjects1.length = 0;
gdjs.MenuCode.GDTelurTerbangObjects2.length = 0;
gdjs.MenuCode.GDTelurTerbangObjects3.length = 0;
gdjs.MenuCode.GDKeranjangObjects1.length = 0;
gdjs.MenuCode.GDKeranjangObjects2.length = 0;
gdjs.MenuCode.GDKeranjangObjects3.length = 0;
gdjs.MenuCode.GDRumputObjects1.length = 0;
gdjs.MenuCode.GDRumputObjects2.length = 0;
gdjs.MenuCode.GDRumputObjects3.length = 0;
gdjs.MenuCode.GDPohonObjects1.length = 0;
gdjs.MenuCode.GDPohonObjects2.length = 0;
gdjs.MenuCode.GDPohonObjects3.length = 0;
gdjs.MenuCode.GDSemakObjects1.length = 0;
gdjs.MenuCode.GDSemakObjects2.length = 0;
gdjs.MenuCode.GDSemakObjects3.length = 0;
gdjs.MenuCode.GDBungaObjects1.length = 0;
gdjs.MenuCode.GDBungaObjects2.length = 0;
gdjs.MenuCode.GDBungaObjects3.length = 0;
gdjs.MenuCode.GDBatuObjects1.length = 0;
gdjs.MenuCode.GDBatuObjects2.length = 0;
gdjs.MenuCode.GDBatuObjects3.length = 0;
gdjs.MenuCode.GDAsapObjects1.length = 0;
gdjs.MenuCode.GDAsapObjects2.length = 0;
gdjs.MenuCode.GDAsapObjects3.length = 0;
gdjs.MenuCode.GDTandaStartObjects1.length = 0;
gdjs.MenuCode.GDTandaStartObjects2.length = 0;
gdjs.MenuCode.GDTandaStartObjects3.length = 0;
gdjs.MenuCode.GDPanelPetaObjects1.length = 0;
gdjs.MenuCode.GDPanelPetaObjects2.length = 0;
gdjs.MenuCode.GDPanelPetaObjects3.length = 0;
gdjs.MenuCode.GDPetaSelObjects1.length = 0;
gdjs.MenuCode.GDPetaSelObjects2.length = 0;
gdjs.MenuCode.GDPetaSelObjects3.length = 0;
gdjs.MenuCode.GDPetaTelurObjects1.length = 0;
gdjs.MenuCode.GDPetaTelurObjects2.length = 0;
gdjs.MenuCode.GDPetaTelurObjects3.length = 0;
gdjs.MenuCode.GDPetaPemainObjects1.length = 0;
gdjs.MenuCode.GDPetaPemainObjects2.length = 0;
gdjs.MenuCode.GDPetaPemainObjects3.length = 0;
gdjs.MenuCode.GDPetaStartObjects1.length = 0;
gdjs.MenuCode.GDPetaStartObjects2.length = 0;
gdjs.MenuCode.GDPetaStartObjects3.length = 0;
gdjs.MenuCode.GDPetaFinishObjects1.length = 0;
gdjs.MenuCode.GDPetaFinishObjects2.length = 0;
gdjs.MenuCode.GDPetaFinishObjects3.length = 0;
gdjs.MenuCode.GDTandaFinishObjects1.length = 0;
gdjs.MenuCode.GDTandaFinishObjects2.length = 0;
gdjs.MenuCode.GDTandaFinishObjects3.length = 0;
gdjs.MenuCode.GDPanahObjects1.length = 0;
gdjs.MenuCode.GDPanahObjects2.length = 0;
gdjs.MenuCode.GDPanahObjects3.length = 0;
gdjs.MenuCode.GDBonekaObjects1.length = 0;
gdjs.MenuCode.GDBonekaObjects2.length = 0;
gdjs.MenuCode.GDBonekaObjects3.length = 0;

gdjs.MenuCode.eventsList5(runtimeScene);
gdjs.MenuCode.GDJudulObjects1.length = 0;
gdjs.MenuCode.GDJudulObjects2.length = 0;
gdjs.MenuCode.GDJudulObjects3.length = 0;
gdjs.MenuCode.GDSubJudulObjects1.length = 0;
gdjs.MenuCode.GDSubJudulObjects2.length = 0;
gdjs.MenuCode.GDSubJudulObjects3.length = 0;
gdjs.MenuCode.GDTombolBabObjects1.length = 0;
gdjs.MenuCode.GDTombolBabObjects2.length = 0;
gdjs.MenuCode.GDTombolBabObjects3.length = 0;
gdjs.MenuCode.GDLabelBabObjects1.length = 0;
gdjs.MenuCode.GDLabelBabObjects2.length = 0;
gdjs.MenuCode.GDLabelBabObjects3.length = 0;
gdjs.MenuCode.GDTombolRakObjects1.length = 0;
gdjs.MenuCode.GDTombolRakObjects2.length = 0;
gdjs.MenuCode.GDTombolRakObjects3.length = 0;
gdjs.MenuCode.GDPetunjukObjects1.length = 0;
gdjs.MenuCode.GDPetunjukObjects2.length = 0;
gdjs.MenuCode.GDPetunjukObjects3.length = 0;
gdjs.MenuCode.GDPetualangObjects1.length = 0;
gdjs.MenuCode.GDPetualangObjects2.length = 0;
gdjs.MenuCode.GDPetualangObjects3.length = 0;
gdjs.MenuCode.GDKepalaPetualangObjects1.length = 0;
gdjs.MenuCode.GDKepalaPetualangObjects2.length = 0;
gdjs.MenuCode.GDKepalaPetualangObjects3.length = 0;
gdjs.MenuCode.GDKelinciObjects1.length = 0;
gdjs.MenuCode.GDKelinciObjects2.length = 0;
gdjs.MenuCode.GDKelinciObjects3.length = 0;
gdjs.MenuCode.GDKepalaKelinciObjects1.length = 0;
gdjs.MenuCode.GDKepalaKelinciObjects2.length = 0;
gdjs.MenuCode.GDKepalaKelinciObjects3.length = 0;
gdjs.MenuCode.GDTelurObjects1.length = 0;
gdjs.MenuCode.GDTelurObjects2.length = 0;
gdjs.MenuCode.GDTelurObjects3.length = 0;
gdjs.MenuCode.GDTelurTerbangObjects1.length = 0;
gdjs.MenuCode.GDTelurTerbangObjects2.length = 0;
gdjs.MenuCode.GDTelurTerbangObjects3.length = 0;
gdjs.MenuCode.GDKeranjangObjects1.length = 0;
gdjs.MenuCode.GDKeranjangObjects2.length = 0;
gdjs.MenuCode.GDKeranjangObjects3.length = 0;
gdjs.MenuCode.GDRumputObjects1.length = 0;
gdjs.MenuCode.GDRumputObjects2.length = 0;
gdjs.MenuCode.GDRumputObjects3.length = 0;
gdjs.MenuCode.GDPohonObjects1.length = 0;
gdjs.MenuCode.GDPohonObjects2.length = 0;
gdjs.MenuCode.GDPohonObjects3.length = 0;
gdjs.MenuCode.GDSemakObjects1.length = 0;
gdjs.MenuCode.GDSemakObjects2.length = 0;
gdjs.MenuCode.GDSemakObjects3.length = 0;
gdjs.MenuCode.GDBungaObjects1.length = 0;
gdjs.MenuCode.GDBungaObjects2.length = 0;
gdjs.MenuCode.GDBungaObjects3.length = 0;
gdjs.MenuCode.GDBatuObjects1.length = 0;
gdjs.MenuCode.GDBatuObjects2.length = 0;
gdjs.MenuCode.GDBatuObjects3.length = 0;
gdjs.MenuCode.GDAsapObjects1.length = 0;
gdjs.MenuCode.GDAsapObjects2.length = 0;
gdjs.MenuCode.GDAsapObjects3.length = 0;
gdjs.MenuCode.GDTandaStartObjects1.length = 0;
gdjs.MenuCode.GDTandaStartObjects2.length = 0;
gdjs.MenuCode.GDTandaStartObjects3.length = 0;
gdjs.MenuCode.GDPanelPetaObjects1.length = 0;
gdjs.MenuCode.GDPanelPetaObjects2.length = 0;
gdjs.MenuCode.GDPanelPetaObjects3.length = 0;
gdjs.MenuCode.GDPetaSelObjects1.length = 0;
gdjs.MenuCode.GDPetaSelObjects2.length = 0;
gdjs.MenuCode.GDPetaSelObjects3.length = 0;
gdjs.MenuCode.GDPetaTelurObjects1.length = 0;
gdjs.MenuCode.GDPetaTelurObjects2.length = 0;
gdjs.MenuCode.GDPetaTelurObjects3.length = 0;
gdjs.MenuCode.GDPetaPemainObjects1.length = 0;
gdjs.MenuCode.GDPetaPemainObjects2.length = 0;
gdjs.MenuCode.GDPetaPemainObjects3.length = 0;
gdjs.MenuCode.GDPetaStartObjects1.length = 0;
gdjs.MenuCode.GDPetaStartObjects2.length = 0;
gdjs.MenuCode.GDPetaStartObjects3.length = 0;
gdjs.MenuCode.GDPetaFinishObjects1.length = 0;
gdjs.MenuCode.GDPetaFinishObjects2.length = 0;
gdjs.MenuCode.GDPetaFinishObjects3.length = 0;
gdjs.MenuCode.GDTandaFinishObjects1.length = 0;
gdjs.MenuCode.GDTandaFinishObjects2.length = 0;
gdjs.MenuCode.GDTandaFinishObjects3.length = 0;
gdjs.MenuCode.GDPanahObjects1.length = 0;
gdjs.MenuCode.GDPanahObjects2.length = 0;
gdjs.MenuCode.GDPanahObjects3.length = 0;
gdjs.MenuCode.GDBonekaObjects1.length = 0;
gdjs.MenuCode.GDBonekaObjects2.length = 0;
gdjs.MenuCode.GDBonekaObjects3.length = 0;


return;

}

gdjs['MenuCode'] = gdjs.MenuCode;
