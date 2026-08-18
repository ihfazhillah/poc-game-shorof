gdjs.KoleksiCode = {};
gdjs.KoleksiCode.localVariables = [];
gdjs.KoleksiCode.idToCallbackMap = new Map();
gdjs.KoleksiCode.forEachIndex3 = 0;

gdjs.KoleksiCode.forEachObjects3 = [];

gdjs.KoleksiCode.forEachTemporary3 = null;

gdjs.KoleksiCode.forEachTotalCount3 = 0;

gdjs.KoleksiCode.GDTeksJudulRakObjects1= [];
gdjs.KoleksiCode.GDTeksJudulRakObjects2= [];
gdjs.KoleksiCode.GDTeksJudulRakObjects3= [];
gdjs.KoleksiCode.GDTeksTotalObjects1= [];
gdjs.KoleksiCode.GDTeksTotalObjects2= [];
gdjs.KoleksiCode.GDTeksTotalObjects3= [];
gdjs.KoleksiCode.GDLabelWazanObjects1= [];
gdjs.KoleksiCode.GDLabelWazanObjects2= [];
gdjs.KoleksiCode.GDLabelWazanObjects3= [];
gdjs.KoleksiCode.GDTeksJumlahObjects1= [];
gdjs.KoleksiCode.GDTeksJumlahObjects2= [];
gdjs.KoleksiCode.GDTeksJumlahObjects3= [];
gdjs.KoleksiCode.GDTombolKembaliObjects1= [];
gdjs.KoleksiCode.GDTombolKembaliObjects2= [];
gdjs.KoleksiCode.GDTombolKembaliObjects3= [];
gdjs.KoleksiCode.GDPetualangObjects1= [];
gdjs.KoleksiCode.GDPetualangObjects2= [];
gdjs.KoleksiCode.GDPetualangObjects3= [];
gdjs.KoleksiCode.GDKepalaPetualangObjects1= [];
gdjs.KoleksiCode.GDKepalaPetualangObjects2= [];
gdjs.KoleksiCode.GDKepalaPetualangObjects3= [];
gdjs.KoleksiCode.GDKelinciObjects1= [];
gdjs.KoleksiCode.GDKelinciObjects2= [];
gdjs.KoleksiCode.GDKelinciObjects3= [];
gdjs.KoleksiCode.GDKepalaKelinciObjects1= [];
gdjs.KoleksiCode.GDKepalaKelinciObjects2= [];
gdjs.KoleksiCode.GDKepalaKelinciObjects3= [];
gdjs.KoleksiCode.GDTelurObjects1= [];
gdjs.KoleksiCode.GDTelurObjects2= [];
gdjs.KoleksiCode.GDTelurObjects3= [];
gdjs.KoleksiCode.GDTelurTerbangObjects1= [];
gdjs.KoleksiCode.GDTelurTerbangObjects2= [];
gdjs.KoleksiCode.GDTelurTerbangObjects3= [];
gdjs.KoleksiCode.GDKeranjangObjects1= [];
gdjs.KoleksiCode.GDKeranjangObjects2= [];
gdjs.KoleksiCode.GDKeranjangObjects3= [];
gdjs.KoleksiCode.GDRumputObjects1= [];
gdjs.KoleksiCode.GDRumputObjects2= [];
gdjs.KoleksiCode.GDRumputObjects3= [];
gdjs.KoleksiCode.GDPohonObjects1= [];
gdjs.KoleksiCode.GDPohonObjects2= [];
gdjs.KoleksiCode.GDPohonObjects3= [];
gdjs.KoleksiCode.GDSemakObjects1= [];
gdjs.KoleksiCode.GDSemakObjects2= [];
gdjs.KoleksiCode.GDSemakObjects3= [];
gdjs.KoleksiCode.GDBungaObjects1= [];
gdjs.KoleksiCode.GDBungaObjects2= [];
gdjs.KoleksiCode.GDBungaObjects3= [];
gdjs.KoleksiCode.GDBatuObjects1= [];
gdjs.KoleksiCode.GDBatuObjects2= [];
gdjs.KoleksiCode.GDBatuObjects3= [];
gdjs.KoleksiCode.GDAsapObjects1= [];
gdjs.KoleksiCode.GDAsapObjects2= [];
gdjs.KoleksiCode.GDAsapObjects3= [];
gdjs.KoleksiCode.GDTandaStartObjects1= [];
gdjs.KoleksiCode.GDTandaStartObjects2= [];
gdjs.KoleksiCode.GDTandaStartObjects3= [];
gdjs.KoleksiCode.GDPanelPetaObjects1= [];
gdjs.KoleksiCode.GDPanelPetaObjects2= [];
gdjs.KoleksiCode.GDPanelPetaObjects3= [];
gdjs.KoleksiCode.GDPetaSelObjects1= [];
gdjs.KoleksiCode.GDPetaSelObjects2= [];
gdjs.KoleksiCode.GDPetaSelObjects3= [];
gdjs.KoleksiCode.GDPetaTelurObjects1= [];
gdjs.KoleksiCode.GDPetaTelurObjects2= [];
gdjs.KoleksiCode.GDPetaTelurObjects3= [];
gdjs.KoleksiCode.GDPetaPemainObjects1= [];
gdjs.KoleksiCode.GDPetaPemainObjects2= [];
gdjs.KoleksiCode.GDPetaPemainObjects3= [];
gdjs.KoleksiCode.GDPetaStartObjects1= [];
gdjs.KoleksiCode.GDPetaStartObjects2= [];
gdjs.KoleksiCode.GDPetaStartObjects3= [];
gdjs.KoleksiCode.GDPetaFinishObjects1= [];
gdjs.KoleksiCode.GDPetaFinishObjects2= [];
gdjs.KoleksiCode.GDPetaFinishObjects3= [];
gdjs.KoleksiCode.GDTandaFinishObjects1= [];
gdjs.KoleksiCode.GDTandaFinishObjects2= [];
gdjs.KoleksiCode.GDTandaFinishObjects3= [];
gdjs.KoleksiCode.GDPanahObjects1= [];
gdjs.KoleksiCode.GDPanahObjects2= [];
gdjs.KoleksiCode.GDPanahObjects3= [];
gdjs.KoleksiCode.GDBonekaObjects1= [];
gdjs.KoleksiCode.GDBonekaObjects2= [];
gdjs.KoleksiCode.GDBonekaObjects3= [];


gdjs.KoleksiCode.eventsList0 = function(runtimeScene) {

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


};gdjs.KoleksiCode.eventsList1 = function(runtimeScene) {

};gdjs.KoleksiCode.eventsList2 = function(runtimeScene) {

};gdjs.KoleksiCode.eventsList3 = function(runtimeScene) {

};gdjs.KoleksiCode.eventsList4 = function(runtimeScene) {

};gdjs.KoleksiCode.eventsList5 = function(runtimeScene) {

{

gdjs.copyArray(runtimeScene.getObjects("Boneka"), gdjs.KoleksiCode.GDBonekaObjects2);

for (gdjs.KoleksiCode.forEachIndex3 = 0;gdjs.KoleksiCode.forEachIndex3 < gdjs.KoleksiCode.GDBonekaObjects2.length;++gdjs.KoleksiCode.forEachIndex3) {
gdjs.KoleksiCode.GDBonekaObjects3.length = 0;


gdjs.KoleksiCode.forEachTemporary3 = gdjs.KoleksiCode.GDBonekaObjects2[gdjs.KoleksiCode.forEachIndex3];
gdjs.KoleksiCode.GDBonekaObjects3.push(gdjs.KoleksiCode.forEachTemporary3);
let isConditionTrue_0 = false;
isConditionTrue_0 = false;
{isConditionTrue_0 = (runtimeScene.getGame().getVariables().getFromIndex(4).getChild(((gdjs.KoleksiCode.GDBonekaObjects3.length === 0 ) ? gdjs.VariablesContainer.badVariablesContainer : gdjs.KoleksiCode.GDBonekaObjects3[0].getVariables()).getFromIndex(0).getAsNumber() - 1).getAsNumber() == 0);
}
if (isConditionTrue_0) {
{for(var i = 0, len = gdjs.KoleksiCode.GDBonekaObjects3.length ;i < len;++i) {
    gdjs.KoleksiCode.GDBonekaObjects3[i].getBehavior("Animation").setAnimationName("kosong");
}
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("Boneka"), gdjs.KoleksiCode.GDBonekaObjects2);

for (gdjs.KoleksiCode.forEachIndex3 = 0;gdjs.KoleksiCode.forEachIndex3 < gdjs.KoleksiCode.GDBonekaObjects2.length;++gdjs.KoleksiCode.forEachIndex3) {
gdjs.KoleksiCode.GDBonekaObjects3.length = 0;


gdjs.KoleksiCode.forEachTemporary3 = gdjs.KoleksiCode.GDBonekaObjects2[gdjs.KoleksiCode.forEachIndex3];
gdjs.KoleksiCode.GDBonekaObjects3.push(gdjs.KoleksiCode.forEachTemporary3);
let isConditionTrue_0 = false;
isConditionTrue_0 = false;
{isConditionTrue_0 = (runtimeScene.getGame().getVariables().getFromIndex(4).getChild(((gdjs.KoleksiCode.GDBonekaObjects3.length === 0 ) ? gdjs.VariablesContainer.badVariablesContainer : gdjs.KoleksiCode.GDBonekaObjects3[0].getVariables()).getFromIndex(0).getAsNumber() - 1).getAsNumber() > 0);
}
if (isConditionTrue_0) {
{for(var i = 0, len = gdjs.KoleksiCode.GDBonekaObjects3.length ;i < len;++i) {
    gdjs.KoleksiCode.GDBonekaObjects3[i].getBehavior("Animation").setAnimationName("b" + gdjs.evtTools.common.toString(gdjs.KoleksiCode.GDBonekaObjects3[i].getVariables().getFromIndex(0).getAsNumber()) + "_t" + gdjs.evtTools.common.toString(gdjs.evtTools.common.clamp(runtimeScene.getGame().getVariables().getFromIndex(4).getChild(gdjs.KoleksiCode.GDBonekaObjects3[i].getVariables().getFromIndex(0).getAsNumber() - 1).getAsNumber(), 1, 4)));
}
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("TeksJumlah"), gdjs.KoleksiCode.GDTeksJumlahObjects2);

for (gdjs.KoleksiCode.forEachIndex3 = 0;gdjs.KoleksiCode.forEachIndex3 < gdjs.KoleksiCode.GDTeksJumlahObjects2.length;++gdjs.KoleksiCode.forEachIndex3) {
gdjs.KoleksiCode.GDTeksJumlahObjects3.length = 0;


gdjs.KoleksiCode.forEachTemporary3 = gdjs.KoleksiCode.GDTeksJumlahObjects2[gdjs.KoleksiCode.forEachIndex3];
gdjs.KoleksiCode.GDTeksJumlahObjects3.push(gdjs.KoleksiCode.forEachTemporary3);
let isConditionTrue_0 = false;
if (true) {
{for(var i = 0, len = gdjs.KoleksiCode.GDTeksJumlahObjects3.length ;i < len;++i) {
    gdjs.KoleksiCode.GDTeksJumlahObjects3[i].getBehavior("Text").setText("x" + gdjs.evtTools.common.toString(runtimeScene.getGame().getVariables().getFromIndex(4).getChild(gdjs.KoleksiCode.GDTeksJumlahObjects3[i].getVariables().getFromIndex(0).getAsNumber() - 1).getAsNumber()));
}
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("LabelWazan"), gdjs.KoleksiCode.GDLabelWazanObjects2);

for (gdjs.KoleksiCode.forEachIndex3 = 0;gdjs.KoleksiCode.forEachIndex3 < gdjs.KoleksiCode.GDLabelWazanObjects2.length;++gdjs.KoleksiCode.forEachIndex3) {
gdjs.KoleksiCode.GDLabelWazanObjects3.length = 0;


gdjs.KoleksiCode.forEachTemporary3 = gdjs.KoleksiCode.GDLabelWazanObjects2[gdjs.KoleksiCode.forEachIndex3];
gdjs.KoleksiCode.GDLabelWazanObjects3.push(gdjs.KoleksiCode.forEachTemporary3);
let isConditionTrue_0 = false;
if (true) {
{for(var i = 0, len = gdjs.KoleksiCode.GDLabelWazanObjects3.length ;i < len;++i) {
    gdjs.KoleksiCode.GDLabelWazanObjects3[i].getBehavior("Text").setText(runtimeScene.getGame().getVariables().getFromIndex(3).getChild(gdjs.KoleksiCode.GDLabelWazanObjects3[i].getVariables().getFromIndex(0).getAsNumber() - 1).getAsString());
}
}
{for(var i = 0, len = gdjs.KoleksiCode.GDLabelWazanObjects3.length ;i < len;++i) {
    gdjs.KoleksiCode.GDLabelWazanObjects3[i].setPadding(20);
}
}
}
}

}


{


let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.runtimeScene.sceneJustBegins(runtimeScene);
if (isConditionTrue_0) {
gdjs.copyArray(runtimeScene.getObjects("TeksTotal"), gdjs.KoleksiCode.GDTeksTotalObjects1);
{for(var i = 0, len = gdjs.KoleksiCode.GDTeksTotalObjects1.length ;i < len;++i) {
    gdjs.KoleksiCode.GDTeksTotalObjects1[i].getBehavior("Text").setText("Semua boneka: x" + gdjs.evtTools.common.toString(runtimeScene.getGame().getVariables().getFromIndex(4).getChild(0).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(1).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(2).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(3).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(4).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(5).getAsNumber()));
}
}
{for(var i = 0, len = gdjs.KoleksiCode.GDTeksTotalObjects1.length ;i < len;++i) {
    gdjs.KoleksiCode.GDTeksTotalObjects1[i].setCenterXInScene(640.0);
}
}
}

}


};gdjs.KoleksiCode.mapOfGDgdjs_9546KoleksiCode_9546GDTombolKembaliObjects1Objects = Hashtable.newFrom({"TombolKembali": gdjs.KoleksiCode.GDTombolKembaliObjects1});
gdjs.KoleksiCode.eventsList6 = function(runtimeScene) {

{


gdjs.KoleksiCode.eventsList0(runtimeScene);
}


{


gdjs.KoleksiCode.eventsList5(runtimeScene);
}


{

gdjs.copyArray(runtimeScene.getObjects("TombolKembali"), gdjs.KoleksiCode.GDTombolKembaliObjects1);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.cursorOnObject(gdjs.KoleksiCode.mapOfGDgdjs_9546KoleksiCode_9546GDTombolKembaliObjects1Objects, runtimeScene, true, false);
if (isConditionTrue_0) {
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.isMouseButtonReleased(runtimeScene, "Left");
}
if (isConditionTrue_0) {
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/sfx/klik.wav", false, 100, 1);
}
{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Menu", false);
}
}

}


};

gdjs.KoleksiCode.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();

gdjs.KoleksiCode.GDTeksJudulRakObjects1.length = 0;
gdjs.KoleksiCode.GDTeksJudulRakObjects2.length = 0;
gdjs.KoleksiCode.GDTeksJudulRakObjects3.length = 0;
gdjs.KoleksiCode.GDTeksTotalObjects1.length = 0;
gdjs.KoleksiCode.GDTeksTotalObjects2.length = 0;
gdjs.KoleksiCode.GDTeksTotalObjects3.length = 0;
gdjs.KoleksiCode.GDLabelWazanObjects1.length = 0;
gdjs.KoleksiCode.GDLabelWazanObjects2.length = 0;
gdjs.KoleksiCode.GDLabelWazanObjects3.length = 0;
gdjs.KoleksiCode.GDTeksJumlahObjects1.length = 0;
gdjs.KoleksiCode.GDTeksJumlahObjects2.length = 0;
gdjs.KoleksiCode.GDTeksJumlahObjects3.length = 0;
gdjs.KoleksiCode.GDTombolKembaliObjects1.length = 0;
gdjs.KoleksiCode.GDTombolKembaliObjects2.length = 0;
gdjs.KoleksiCode.GDTombolKembaliObjects3.length = 0;
gdjs.KoleksiCode.GDPetualangObjects1.length = 0;
gdjs.KoleksiCode.GDPetualangObjects2.length = 0;
gdjs.KoleksiCode.GDPetualangObjects3.length = 0;
gdjs.KoleksiCode.GDKepalaPetualangObjects1.length = 0;
gdjs.KoleksiCode.GDKepalaPetualangObjects2.length = 0;
gdjs.KoleksiCode.GDKepalaPetualangObjects3.length = 0;
gdjs.KoleksiCode.GDKelinciObjects1.length = 0;
gdjs.KoleksiCode.GDKelinciObjects2.length = 0;
gdjs.KoleksiCode.GDKelinciObjects3.length = 0;
gdjs.KoleksiCode.GDKepalaKelinciObjects1.length = 0;
gdjs.KoleksiCode.GDKepalaKelinciObjects2.length = 0;
gdjs.KoleksiCode.GDKepalaKelinciObjects3.length = 0;
gdjs.KoleksiCode.GDTelurObjects1.length = 0;
gdjs.KoleksiCode.GDTelurObjects2.length = 0;
gdjs.KoleksiCode.GDTelurObjects3.length = 0;
gdjs.KoleksiCode.GDTelurTerbangObjects1.length = 0;
gdjs.KoleksiCode.GDTelurTerbangObjects2.length = 0;
gdjs.KoleksiCode.GDTelurTerbangObjects3.length = 0;
gdjs.KoleksiCode.GDKeranjangObjects1.length = 0;
gdjs.KoleksiCode.GDKeranjangObjects2.length = 0;
gdjs.KoleksiCode.GDKeranjangObjects3.length = 0;
gdjs.KoleksiCode.GDRumputObjects1.length = 0;
gdjs.KoleksiCode.GDRumputObjects2.length = 0;
gdjs.KoleksiCode.GDRumputObjects3.length = 0;
gdjs.KoleksiCode.GDPohonObjects1.length = 0;
gdjs.KoleksiCode.GDPohonObjects2.length = 0;
gdjs.KoleksiCode.GDPohonObjects3.length = 0;
gdjs.KoleksiCode.GDSemakObjects1.length = 0;
gdjs.KoleksiCode.GDSemakObjects2.length = 0;
gdjs.KoleksiCode.GDSemakObjects3.length = 0;
gdjs.KoleksiCode.GDBungaObjects1.length = 0;
gdjs.KoleksiCode.GDBungaObjects2.length = 0;
gdjs.KoleksiCode.GDBungaObjects3.length = 0;
gdjs.KoleksiCode.GDBatuObjects1.length = 0;
gdjs.KoleksiCode.GDBatuObjects2.length = 0;
gdjs.KoleksiCode.GDBatuObjects3.length = 0;
gdjs.KoleksiCode.GDAsapObjects1.length = 0;
gdjs.KoleksiCode.GDAsapObjects2.length = 0;
gdjs.KoleksiCode.GDAsapObjects3.length = 0;
gdjs.KoleksiCode.GDTandaStartObjects1.length = 0;
gdjs.KoleksiCode.GDTandaStartObjects2.length = 0;
gdjs.KoleksiCode.GDTandaStartObjects3.length = 0;
gdjs.KoleksiCode.GDPanelPetaObjects1.length = 0;
gdjs.KoleksiCode.GDPanelPetaObjects2.length = 0;
gdjs.KoleksiCode.GDPanelPetaObjects3.length = 0;
gdjs.KoleksiCode.GDPetaSelObjects1.length = 0;
gdjs.KoleksiCode.GDPetaSelObjects2.length = 0;
gdjs.KoleksiCode.GDPetaSelObjects3.length = 0;
gdjs.KoleksiCode.GDPetaTelurObjects1.length = 0;
gdjs.KoleksiCode.GDPetaTelurObjects2.length = 0;
gdjs.KoleksiCode.GDPetaTelurObjects3.length = 0;
gdjs.KoleksiCode.GDPetaPemainObjects1.length = 0;
gdjs.KoleksiCode.GDPetaPemainObjects2.length = 0;
gdjs.KoleksiCode.GDPetaPemainObjects3.length = 0;
gdjs.KoleksiCode.GDPetaStartObjects1.length = 0;
gdjs.KoleksiCode.GDPetaStartObjects2.length = 0;
gdjs.KoleksiCode.GDPetaStartObjects3.length = 0;
gdjs.KoleksiCode.GDPetaFinishObjects1.length = 0;
gdjs.KoleksiCode.GDPetaFinishObjects2.length = 0;
gdjs.KoleksiCode.GDPetaFinishObjects3.length = 0;
gdjs.KoleksiCode.GDTandaFinishObjects1.length = 0;
gdjs.KoleksiCode.GDTandaFinishObjects2.length = 0;
gdjs.KoleksiCode.GDTandaFinishObjects3.length = 0;
gdjs.KoleksiCode.GDPanahObjects1.length = 0;
gdjs.KoleksiCode.GDPanahObjects2.length = 0;
gdjs.KoleksiCode.GDPanahObjects3.length = 0;
gdjs.KoleksiCode.GDBonekaObjects1.length = 0;
gdjs.KoleksiCode.GDBonekaObjects2.length = 0;
gdjs.KoleksiCode.GDBonekaObjects3.length = 0;

gdjs.KoleksiCode.eventsList6(runtimeScene);
gdjs.KoleksiCode.GDTeksJudulRakObjects1.length = 0;
gdjs.KoleksiCode.GDTeksJudulRakObjects2.length = 0;
gdjs.KoleksiCode.GDTeksJudulRakObjects3.length = 0;
gdjs.KoleksiCode.GDTeksTotalObjects1.length = 0;
gdjs.KoleksiCode.GDTeksTotalObjects2.length = 0;
gdjs.KoleksiCode.GDTeksTotalObjects3.length = 0;
gdjs.KoleksiCode.GDLabelWazanObjects1.length = 0;
gdjs.KoleksiCode.GDLabelWazanObjects2.length = 0;
gdjs.KoleksiCode.GDLabelWazanObjects3.length = 0;
gdjs.KoleksiCode.GDTeksJumlahObjects1.length = 0;
gdjs.KoleksiCode.GDTeksJumlahObjects2.length = 0;
gdjs.KoleksiCode.GDTeksJumlahObjects3.length = 0;
gdjs.KoleksiCode.GDTombolKembaliObjects1.length = 0;
gdjs.KoleksiCode.GDTombolKembaliObjects2.length = 0;
gdjs.KoleksiCode.GDTombolKembaliObjects3.length = 0;
gdjs.KoleksiCode.GDPetualangObjects1.length = 0;
gdjs.KoleksiCode.GDPetualangObjects2.length = 0;
gdjs.KoleksiCode.GDPetualangObjects3.length = 0;
gdjs.KoleksiCode.GDKepalaPetualangObjects1.length = 0;
gdjs.KoleksiCode.GDKepalaPetualangObjects2.length = 0;
gdjs.KoleksiCode.GDKepalaPetualangObjects3.length = 0;
gdjs.KoleksiCode.GDKelinciObjects1.length = 0;
gdjs.KoleksiCode.GDKelinciObjects2.length = 0;
gdjs.KoleksiCode.GDKelinciObjects3.length = 0;
gdjs.KoleksiCode.GDKepalaKelinciObjects1.length = 0;
gdjs.KoleksiCode.GDKepalaKelinciObjects2.length = 0;
gdjs.KoleksiCode.GDKepalaKelinciObjects3.length = 0;
gdjs.KoleksiCode.GDTelurObjects1.length = 0;
gdjs.KoleksiCode.GDTelurObjects2.length = 0;
gdjs.KoleksiCode.GDTelurObjects3.length = 0;
gdjs.KoleksiCode.GDTelurTerbangObjects1.length = 0;
gdjs.KoleksiCode.GDTelurTerbangObjects2.length = 0;
gdjs.KoleksiCode.GDTelurTerbangObjects3.length = 0;
gdjs.KoleksiCode.GDKeranjangObjects1.length = 0;
gdjs.KoleksiCode.GDKeranjangObjects2.length = 0;
gdjs.KoleksiCode.GDKeranjangObjects3.length = 0;
gdjs.KoleksiCode.GDRumputObjects1.length = 0;
gdjs.KoleksiCode.GDRumputObjects2.length = 0;
gdjs.KoleksiCode.GDRumputObjects3.length = 0;
gdjs.KoleksiCode.GDPohonObjects1.length = 0;
gdjs.KoleksiCode.GDPohonObjects2.length = 0;
gdjs.KoleksiCode.GDPohonObjects3.length = 0;
gdjs.KoleksiCode.GDSemakObjects1.length = 0;
gdjs.KoleksiCode.GDSemakObjects2.length = 0;
gdjs.KoleksiCode.GDSemakObjects3.length = 0;
gdjs.KoleksiCode.GDBungaObjects1.length = 0;
gdjs.KoleksiCode.GDBungaObjects2.length = 0;
gdjs.KoleksiCode.GDBungaObjects3.length = 0;
gdjs.KoleksiCode.GDBatuObjects1.length = 0;
gdjs.KoleksiCode.GDBatuObjects2.length = 0;
gdjs.KoleksiCode.GDBatuObjects3.length = 0;
gdjs.KoleksiCode.GDAsapObjects1.length = 0;
gdjs.KoleksiCode.GDAsapObjects2.length = 0;
gdjs.KoleksiCode.GDAsapObjects3.length = 0;
gdjs.KoleksiCode.GDTandaStartObjects1.length = 0;
gdjs.KoleksiCode.GDTandaStartObjects2.length = 0;
gdjs.KoleksiCode.GDTandaStartObjects3.length = 0;
gdjs.KoleksiCode.GDPanelPetaObjects1.length = 0;
gdjs.KoleksiCode.GDPanelPetaObjects2.length = 0;
gdjs.KoleksiCode.GDPanelPetaObjects3.length = 0;
gdjs.KoleksiCode.GDPetaSelObjects1.length = 0;
gdjs.KoleksiCode.GDPetaSelObjects2.length = 0;
gdjs.KoleksiCode.GDPetaSelObjects3.length = 0;
gdjs.KoleksiCode.GDPetaTelurObjects1.length = 0;
gdjs.KoleksiCode.GDPetaTelurObjects2.length = 0;
gdjs.KoleksiCode.GDPetaTelurObjects3.length = 0;
gdjs.KoleksiCode.GDPetaPemainObjects1.length = 0;
gdjs.KoleksiCode.GDPetaPemainObjects2.length = 0;
gdjs.KoleksiCode.GDPetaPemainObjects3.length = 0;
gdjs.KoleksiCode.GDPetaStartObjects1.length = 0;
gdjs.KoleksiCode.GDPetaStartObjects2.length = 0;
gdjs.KoleksiCode.GDPetaStartObjects3.length = 0;
gdjs.KoleksiCode.GDPetaFinishObjects1.length = 0;
gdjs.KoleksiCode.GDPetaFinishObjects2.length = 0;
gdjs.KoleksiCode.GDPetaFinishObjects3.length = 0;
gdjs.KoleksiCode.GDTandaFinishObjects1.length = 0;
gdjs.KoleksiCode.GDTandaFinishObjects2.length = 0;
gdjs.KoleksiCode.GDTandaFinishObjects3.length = 0;
gdjs.KoleksiCode.GDPanahObjects1.length = 0;
gdjs.KoleksiCode.GDPanahObjects2.length = 0;
gdjs.KoleksiCode.GDPanahObjects3.length = 0;
gdjs.KoleksiCode.GDBonekaObjects1.length = 0;
gdjs.KoleksiCode.GDBonekaObjects2.length = 0;
gdjs.KoleksiCode.GDBonekaObjects3.length = 0;


return;

}

gdjs['KoleksiCode'] = gdjs.KoleksiCode;
