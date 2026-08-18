gdjs.MenangCode = {};
gdjs.MenangCode.localVariables = [];
gdjs.MenangCode.idToCallbackMap = new Map();
gdjs.MenangCode.GDTeksHebatObjects1= [];
gdjs.MenangCode.GDTeksHebatObjects2= [];
gdjs.MenangCode.GDTeksHebatObjects3= [];
gdjs.MenangCode.GDTeksMenangObjects1= [];
gdjs.MenangCode.GDTeksMenangObjects2= [];
gdjs.MenangCode.GDTeksMenangObjects3= [];
gdjs.MenangCode.GDTeksJumlahBonekaObjects1= [];
gdjs.MenangCode.GDTeksJumlahBonekaObjects2= [];
gdjs.MenangCode.GDTeksJumlahBonekaObjects3= [];
gdjs.MenangCode.GDTombolLagiObjects1= [];
gdjs.MenangCode.GDTombolLagiObjects2= [];
gdjs.MenangCode.GDTombolLagiObjects3= [];
gdjs.MenangCode.GDTombolRakObjects1= [];
gdjs.MenangCode.GDTombolRakObjects2= [];
gdjs.MenangCode.GDTombolRakObjects3= [];
gdjs.MenangCode.GDPetualangObjects1= [];
gdjs.MenangCode.GDPetualangObjects2= [];
gdjs.MenangCode.GDPetualangObjects3= [];
gdjs.MenangCode.GDKepalaPetualangObjects1= [];
gdjs.MenangCode.GDKepalaPetualangObjects2= [];
gdjs.MenangCode.GDKepalaPetualangObjects3= [];
gdjs.MenangCode.GDKelinciObjects1= [];
gdjs.MenangCode.GDKelinciObjects2= [];
gdjs.MenangCode.GDKelinciObjects3= [];
gdjs.MenangCode.GDKepalaKelinciObjects1= [];
gdjs.MenangCode.GDKepalaKelinciObjects2= [];
gdjs.MenangCode.GDKepalaKelinciObjects3= [];
gdjs.MenangCode.GDTelurObjects1= [];
gdjs.MenangCode.GDTelurObjects2= [];
gdjs.MenangCode.GDTelurObjects3= [];
gdjs.MenangCode.GDTelurTerbangObjects1= [];
gdjs.MenangCode.GDTelurTerbangObjects2= [];
gdjs.MenangCode.GDTelurTerbangObjects3= [];
gdjs.MenangCode.GDKeranjangObjects1= [];
gdjs.MenangCode.GDKeranjangObjects2= [];
gdjs.MenangCode.GDKeranjangObjects3= [];
gdjs.MenangCode.GDRumputObjects1= [];
gdjs.MenangCode.GDRumputObjects2= [];
gdjs.MenangCode.GDRumputObjects3= [];
gdjs.MenangCode.GDPohonObjects1= [];
gdjs.MenangCode.GDPohonObjects2= [];
gdjs.MenangCode.GDPohonObjects3= [];
gdjs.MenangCode.GDSemakObjects1= [];
gdjs.MenangCode.GDSemakObjects2= [];
gdjs.MenangCode.GDSemakObjects3= [];
gdjs.MenangCode.GDBungaObjects1= [];
gdjs.MenangCode.GDBungaObjects2= [];
gdjs.MenangCode.GDBungaObjects3= [];
gdjs.MenangCode.GDBatuObjects1= [];
gdjs.MenangCode.GDBatuObjects2= [];
gdjs.MenangCode.GDBatuObjects3= [];
gdjs.MenangCode.GDAsapObjects1= [];
gdjs.MenangCode.GDAsapObjects2= [];
gdjs.MenangCode.GDAsapObjects3= [];
gdjs.MenangCode.GDTandaStartObjects1= [];
gdjs.MenangCode.GDTandaStartObjects2= [];
gdjs.MenangCode.GDTandaStartObjects3= [];
gdjs.MenangCode.GDPanelPetaObjects1= [];
gdjs.MenangCode.GDPanelPetaObjects2= [];
gdjs.MenangCode.GDPanelPetaObjects3= [];
gdjs.MenangCode.GDPetaSelObjects1= [];
gdjs.MenangCode.GDPetaSelObjects2= [];
gdjs.MenangCode.GDPetaSelObjects3= [];
gdjs.MenangCode.GDPetaTelurObjects1= [];
gdjs.MenangCode.GDPetaTelurObjects2= [];
gdjs.MenangCode.GDPetaTelurObjects3= [];
gdjs.MenangCode.GDPetaPemainObjects1= [];
gdjs.MenangCode.GDPetaPemainObjects2= [];
gdjs.MenangCode.GDPetaPemainObjects3= [];
gdjs.MenangCode.GDPetaStartObjects1= [];
gdjs.MenangCode.GDPetaStartObjects2= [];
gdjs.MenangCode.GDPetaStartObjects3= [];
gdjs.MenangCode.GDPetaFinishObjects1= [];
gdjs.MenangCode.GDPetaFinishObjects2= [];
gdjs.MenangCode.GDPetaFinishObjects3= [];
gdjs.MenangCode.GDTandaFinishObjects1= [];
gdjs.MenangCode.GDTandaFinishObjects2= [];
gdjs.MenangCode.GDTandaFinishObjects3= [];
gdjs.MenangCode.GDPanahObjects1= [];
gdjs.MenangCode.GDPanahObjects2= [];
gdjs.MenangCode.GDPanahObjects3= [];
gdjs.MenangCode.GDBonekaObjects1= [];
gdjs.MenangCode.GDBonekaObjects2= [];
gdjs.MenangCode.GDBonekaObjects3= [];


gdjs.MenangCode.eventsList0 = function(runtimeScene) {

{


let isConditionTrue_0 = false;
{
gdjs.copyArray(runtimeScene.getObjects("Kelinci"), gdjs.MenangCode.GDKelinciObjects1);
gdjs.copyArray(runtimeScene.getObjects("KepalaKelinci"), gdjs.MenangCode.GDKepalaKelinciObjects1);
gdjs.copyArray(runtimeScene.getObjects("KepalaPetualang"), gdjs.MenangCode.GDKepalaPetualangObjects1);
gdjs.copyArray(runtimeScene.getObjects("Petualang"), gdjs.MenangCode.GDPetualangObjects1);
{for(var i = 0, len = gdjs.MenangCode.GDKepalaPetualangObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDKepalaPetualangObjects1[i].setX((( gdjs.MenangCode.GDPetualangObjects1.length === 0 ) ? 0 :gdjs.MenangCode.GDPetualangObjects1[0].getPointX("")) + 4);
}
}
{for(var i = 0, len = gdjs.MenangCode.GDKepalaPetualangObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDKepalaPetualangObjects1[i].setY((( gdjs.MenangCode.GDPetualangObjects1.length === 0 ) ? 0 :gdjs.MenangCode.GDPetualangObjects1[0].getPointY("")) - 50);
}
}
{for(var i = 0, len = gdjs.MenangCode.GDKepalaKelinciObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDKepalaKelinciObjects1[i].setX((( gdjs.MenangCode.GDKelinciObjects1.length === 0 ) ? 0 :gdjs.MenangCode.GDKelinciObjects1[0].getPointX("")) - 4);
}
}
{for(var i = 0, len = gdjs.MenangCode.GDKepalaKelinciObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDKepalaKelinciObjects1[i].setY((( gdjs.MenangCode.GDKelinciObjects1.length === 0 ) ? 0 :gdjs.MenangCode.GDKelinciObjects1[0].getPointY("")) - 62);
}
}
}

}


};gdjs.MenangCode.mapOfGDgdjs_9546MenangCode_9546GDAsapObjects2Objects = Hashtable.newFrom({"Asap": gdjs.MenangCode.GDAsapObjects2});
gdjs.MenangCode.eventsList1 = function(runtimeScene) {

{


let isConditionTrue_0 = false;
isConditionTrue_0 = false;
{isConditionTrue_0 = (runtimeScene.getScene().getVariables().getFromIndex(0).getAsNumber() == 0);
}
if (isConditionTrue_0) {
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.runtimeScene.getTimerElapsedTimeInSecondsOrNaN(runtimeScene, "menang") > 1.2;
}
if (isConditionTrue_0) {
gdjs.copyArray(runtimeScene.getObjects("Boneka"), gdjs.MenangCode.GDBonekaObjects2);
gdjs.copyArray(runtimeScene.getObjects("Kelinci"), gdjs.MenangCode.GDKelinciObjects2);
gdjs.copyArray(runtimeScene.getObjects("KepalaKelinci"), gdjs.MenangCode.GDKepalaKelinciObjects2);
gdjs.MenangCode.GDAsapObjects2.length = 0;

{runtimeScene.getScene().getVariables().getFromIndex(0).setNumber(1);
}
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/sfx/pop.wav", false, 100, 1);
}
{gdjs.evtTools.object.createObjectOnScene(runtimeScene, gdjs.MenangCode.mapOfGDgdjs_9546MenangCode_9546GDAsapObjects2Objects, (( gdjs.MenangCode.GDKelinciObjects2.length === 0 ) ? 0 :gdjs.MenangCode.GDKelinciObjects2[0].getPointX("")) - 16, (( gdjs.MenangCode.GDKelinciObjects2.length === 0 ) ? 0 :gdjs.MenangCode.GDKelinciObjects2[0].getPointY("")) - 40, "");
}
{for(var i = 0, len = gdjs.MenangCode.GDKelinciObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDKelinciObjects2[i].hide();
}
}
{for(var i = 0, len = gdjs.MenangCode.GDKepalaKelinciObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDKepalaKelinciObjects2[i].hide();
}
}
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects2[i].hide(false);
}
}
{gdjs.evtTools.sound.playSoundOnChannel(runtimeScene, "audio/suara/boneka.mp3", 3, false, 100, 1);
}
}

}


{


let isConditionTrue_0 = false;
isConditionTrue_0 = false;
{isConditionTrue_0 = (runtimeScene.getScene().getVariables().getFromIndex(0).getAsNumber() == 1);
}
if (isConditionTrue_0) {
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.runtimeScene.getTimerElapsedTimeInSecondsOrNaN(runtimeScene, "menang") > 2.6;
}
if (isConditionTrue_0) {
gdjs.copyArray(runtimeScene.getObjects("Boneka"), gdjs.MenangCode.GDBonekaObjects2);
gdjs.copyArray(runtimeScene.getObjects("TombolRak"), gdjs.MenangCode.GDTombolRakObjects2);
{runtimeScene.getScene().getVariables().getFromIndex(0).setNumber(2);
}
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects2[i].getBehavior("Tween").addObjectPositionTween2("masukRak", (( gdjs.MenangCode.GDTombolRakObjects2.length === 0 ) ? 0 :gdjs.MenangCode.GDTombolRakObjects2[0].getCenterXInScene()) - (gdjs.MenangCode.GDBonekaObjects2[i].getWidth()) / 2, (( gdjs.MenangCode.GDTombolRakObjects2.length === 0 ) ? 0 :gdjs.MenangCode.GDTombolRakObjects2[0].getCenterYInScene()) - (gdjs.MenangCode.GDBonekaObjects2[i].getHeight()) / 2, "easeInQuad", 1, false);
}
}
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects2[i].getBehavior("Tween").addObjectScaleTween3("mengecil", 0.35, "easeInQuad", 1, false, true);
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("Boneka"), gdjs.MenangCode.GDBonekaObjects2);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
for (var i = 0, k = 0, l = gdjs.MenangCode.GDBonekaObjects2.length;i<l;++i) {
    if ( gdjs.MenangCode.GDBonekaObjects2[i].getBehavior("Tween").hasFinished("masukRak") ) {
        isConditionTrue_0 = true;
        gdjs.MenangCode.GDBonekaObjects2[k] = gdjs.MenangCode.GDBonekaObjects2[i];
        ++k;
    }
}
gdjs.MenangCode.GDBonekaObjects2.length = k;
if (isConditionTrue_0) {
/* Reuse gdjs.MenangCode.GDBonekaObjects2 */
gdjs.copyArray(runtimeScene.getObjects("TeksJumlahBoneka"), gdjs.MenangCode.GDTeksJumlahBonekaObjects2);
gdjs.copyArray(runtimeScene.getObjects("TombolRak"), gdjs.MenangCode.GDTombolRakObjects2);
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects2[i].getBehavior("Tween").removeTween("masukRak");
}
}
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects2[i].hide();
}
}
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/sfx/ding.wav", false, 100, 1);
}
{for(var i = 0, len = gdjs.MenangCode.GDTeksJumlahBonekaObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDTeksJumlahBonekaObjects2[i].hide(false);
}
}
{for(var i = 0, len = gdjs.MenangCode.GDTombolRakObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDTombolRakObjects2[i].getBehavior("Tween").addObjectScaleTween3("besar", 1.15, "easeOutQuad", 0.12, false, true);
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("TombolRak"), gdjs.MenangCode.GDTombolRakObjects2);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
for (var i = 0, k = 0, l = gdjs.MenangCode.GDTombolRakObjects2.length;i<l;++i) {
    if ( gdjs.MenangCode.GDTombolRakObjects2[i].getBehavior("Tween").hasFinished("besar") ) {
        isConditionTrue_0 = true;
        gdjs.MenangCode.GDTombolRakObjects2[k] = gdjs.MenangCode.GDTombolRakObjects2[i];
        ++k;
    }
}
gdjs.MenangCode.GDTombolRakObjects2.length = k;
if (isConditionTrue_0) {
/* Reuse gdjs.MenangCode.GDTombolRakObjects2 */
{for(var i = 0, len = gdjs.MenangCode.GDTombolRakObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDTombolRakObjects2[i].getBehavior("Tween").removeTween("besar");
}
}
{for(var i = 0, len = gdjs.MenangCode.GDTombolRakObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDTombolRakObjects2[i].getBehavior("Tween").addObjectScaleTween3("kecil", 1, "easeInQuad", 0.15, false, true);
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("TombolRak"), gdjs.MenangCode.GDTombolRakObjects2);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
for (var i = 0, k = 0, l = gdjs.MenangCode.GDTombolRakObjects2.length;i<l;++i) {
    if ( gdjs.MenangCode.GDTombolRakObjects2[i].getBehavior("Tween").hasFinished("kecil") ) {
        isConditionTrue_0 = true;
        gdjs.MenangCode.GDTombolRakObjects2[k] = gdjs.MenangCode.GDTombolRakObjects2[i];
        ++k;
    }
}
gdjs.MenangCode.GDTombolRakObjects2.length = k;
if (isConditionTrue_0) {
/* Reuse gdjs.MenangCode.GDTombolRakObjects2 */
{for(var i = 0, len = gdjs.MenangCode.GDTombolRakObjects2.length ;i < len;++i) {
    gdjs.MenangCode.GDTombolRakObjects2[i].getBehavior("Tween").removeTween("kecil");
}
}
}

}


{

gdjs.copyArray(runtimeScene.getObjects("Asap"), gdjs.MenangCode.GDAsapObjects1);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
for (var i = 0, k = 0, l = gdjs.MenangCode.GDAsapObjects1.length;i<l;++i) {
    if ( gdjs.MenangCode.GDAsapObjects1[i].getBehavior("Animation").hasAnimationEnded() ) {
        isConditionTrue_0 = true;
        gdjs.MenangCode.GDAsapObjects1[k] = gdjs.MenangCode.GDAsapObjects1[i];
        ++k;
    }
}
gdjs.MenangCode.GDAsapObjects1.length = k;
if (isConditionTrue_0) {
/* Reuse gdjs.MenangCode.GDAsapObjects1 */
{for(var i = 0, len = gdjs.MenangCode.GDAsapObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDAsapObjects1[i].deleteFromScene(runtimeScene);
}
}
}

}


};gdjs.MenangCode.mapOfGDgdjs_9546MenangCode_9546GDTombolLagiObjects1Objects = Hashtable.newFrom({"TombolLagi": gdjs.MenangCode.GDTombolLagiObjects1});
gdjs.MenangCode.mapOfGDgdjs_9546MenangCode_9546GDTombolRakObjects1Objects = Hashtable.newFrom({"TombolRak": gdjs.MenangCode.GDTombolRakObjects1});
gdjs.MenangCode.eventsList2 = function(runtimeScene) {

{


let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.runtimeScene.sceneJustBegins(runtimeScene);
if (isConditionTrue_0) {
gdjs.copyArray(runtimeScene.getObjects("Boneka"), gdjs.MenangCode.GDBonekaObjects1);
gdjs.copyArray(runtimeScene.getObjects("KepalaKelinci"), gdjs.MenangCode.GDKepalaKelinciObjects1);
gdjs.copyArray(runtimeScene.getObjects("TeksJumlahBoneka"), gdjs.MenangCode.GDTeksJumlahBonekaObjects1);
{gdjs.evtTools.runtimeScene.resetTimer(runtimeScene, "menang");
}
{runtimeScene.getScene().getVariables().getFromIndex(0).setNumber(0);
}
{runtimeScene.getGame().getVariables().getFromIndex(4).getChild(runtimeScene.getGame().getVariables().getFromIndex(2).getAsNumber() - 1).add(1);
}
{gdjs.evtTools.storage.writeStringInJSONFile("TelurWazan", "koleksi", gdjs.evtTools.network.variableStructureToJSON(runtimeScene.getGame().getVariables().getFromIndex(4)));
}
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects1[i].getBehavior("Animation").setAnimationName("b" + gdjs.evtTools.common.toString(runtimeScene.getGame().getVariables().getFromIndex(2).getAsNumber()) + "_t" + gdjs.evtTools.common.toString(gdjs.evtTools.common.clamp(runtimeScene.getGame().getVariables().getFromIndex(4).getChild(runtimeScene.getGame().getVariables().getFromIndex(2).getAsNumber() - 1).getAsNumber(), 1, 4)));
}
}
{for(var i = 0, len = gdjs.MenangCode.GDBonekaObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDBonekaObjects1[i].hide();
}
}
{for(var i = 0, len = gdjs.MenangCode.GDTeksJumlahBonekaObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDTeksJumlahBonekaObjects1[i].hide();
}
}
{for(var i = 0, len = gdjs.MenangCode.GDKepalaKelinciObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDKepalaKelinciObjects1[i].getBehavior("Animation").setAnimationName("biasa");
}
}
{for(var i = 0, len = gdjs.MenangCode.GDTeksJumlahBonekaObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDTeksJumlahBonekaObjects1[i].getBehavior("Text").setText("Boneka wazan ini: x" + gdjs.evtTools.common.toString(runtimeScene.getGame().getVariables().getFromIndex(4).getChild(runtimeScene.getGame().getVariables().getFromIndex(2).getAsNumber() - 1).getAsNumber()) + "   •   Semua boneka: x" + gdjs.evtTools.common.toString(runtimeScene.getGame().getVariables().getFromIndex(4).getChild(0).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(1).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(2).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(3).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(4).getAsNumber() + runtimeScene.getGame().getVariables().getFromIndex(4).getChild(5).getAsNumber()));
}
}
{for(var i = 0, len = gdjs.MenangCode.GDTeksJumlahBonekaObjects1.length ;i < len;++i) {
    gdjs.MenangCode.GDTeksJumlahBonekaObjects1[i].setCenterXInScene(640.0);
}
}
{gdjs.evtTools.sound.playSound(runtimeScene, "audio/sfx/menang.wav", false, 100, 1);
}
}

}


{


gdjs.MenangCode.eventsList0(runtimeScene);
}


{


gdjs.MenangCode.eventsList1(runtimeScene);
}


{

gdjs.copyArray(runtimeScene.getObjects("TombolLagi"), gdjs.MenangCode.GDTombolLagiObjects1);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.cursorOnObject(gdjs.MenangCode.mapOfGDgdjs_9546MenangCode_9546GDTombolLagiObjects1Objects, runtimeScene, true, false);
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


{

gdjs.copyArray(runtimeScene.getObjects("TombolRak"), gdjs.MenangCode.GDTombolRakObjects1);

let isConditionTrue_0 = false;
isConditionTrue_0 = false;
isConditionTrue_0 = gdjs.evtTools.input.cursorOnObject(gdjs.MenangCode.mapOfGDgdjs_9546MenangCode_9546GDTombolRakObjects1Objects, runtimeScene, true, false);
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


};

gdjs.MenangCode.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();

gdjs.MenangCode.GDTeksHebatObjects1.length = 0;
gdjs.MenangCode.GDTeksHebatObjects2.length = 0;
gdjs.MenangCode.GDTeksHebatObjects3.length = 0;
gdjs.MenangCode.GDTeksMenangObjects1.length = 0;
gdjs.MenangCode.GDTeksMenangObjects2.length = 0;
gdjs.MenangCode.GDTeksMenangObjects3.length = 0;
gdjs.MenangCode.GDTeksJumlahBonekaObjects1.length = 0;
gdjs.MenangCode.GDTeksJumlahBonekaObjects2.length = 0;
gdjs.MenangCode.GDTeksJumlahBonekaObjects3.length = 0;
gdjs.MenangCode.GDTombolLagiObjects1.length = 0;
gdjs.MenangCode.GDTombolLagiObjects2.length = 0;
gdjs.MenangCode.GDTombolLagiObjects3.length = 0;
gdjs.MenangCode.GDTombolRakObjects1.length = 0;
gdjs.MenangCode.GDTombolRakObjects2.length = 0;
gdjs.MenangCode.GDTombolRakObjects3.length = 0;
gdjs.MenangCode.GDPetualangObjects1.length = 0;
gdjs.MenangCode.GDPetualangObjects2.length = 0;
gdjs.MenangCode.GDPetualangObjects3.length = 0;
gdjs.MenangCode.GDKepalaPetualangObjects1.length = 0;
gdjs.MenangCode.GDKepalaPetualangObjects2.length = 0;
gdjs.MenangCode.GDKepalaPetualangObjects3.length = 0;
gdjs.MenangCode.GDKelinciObjects1.length = 0;
gdjs.MenangCode.GDKelinciObjects2.length = 0;
gdjs.MenangCode.GDKelinciObjects3.length = 0;
gdjs.MenangCode.GDKepalaKelinciObjects1.length = 0;
gdjs.MenangCode.GDKepalaKelinciObjects2.length = 0;
gdjs.MenangCode.GDKepalaKelinciObjects3.length = 0;
gdjs.MenangCode.GDTelurObjects1.length = 0;
gdjs.MenangCode.GDTelurObjects2.length = 0;
gdjs.MenangCode.GDTelurObjects3.length = 0;
gdjs.MenangCode.GDTelurTerbangObjects1.length = 0;
gdjs.MenangCode.GDTelurTerbangObjects2.length = 0;
gdjs.MenangCode.GDTelurTerbangObjects3.length = 0;
gdjs.MenangCode.GDKeranjangObjects1.length = 0;
gdjs.MenangCode.GDKeranjangObjects2.length = 0;
gdjs.MenangCode.GDKeranjangObjects3.length = 0;
gdjs.MenangCode.GDRumputObjects1.length = 0;
gdjs.MenangCode.GDRumputObjects2.length = 0;
gdjs.MenangCode.GDRumputObjects3.length = 0;
gdjs.MenangCode.GDPohonObjects1.length = 0;
gdjs.MenangCode.GDPohonObjects2.length = 0;
gdjs.MenangCode.GDPohonObjects3.length = 0;
gdjs.MenangCode.GDSemakObjects1.length = 0;
gdjs.MenangCode.GDSemakObjects2.length = 0;
gdjs.MenangCode.GDSemakObjects3.length = 0;
gdjs.MenangCode.GDBungaObjects1.length = 0;
gdjs.MenangCode.GDBungaObjects2.length = 0;
gdjs.MenangCode.GDBungaObjects3.length = 0;
gdjs.MenangCode.GDBatuObjects1.length = 0;
gdjs.MenangCode.GDBatuObjects2.length = 0;
gdjs.MenangCode.GDBatuObjects3.length = 0;
gdjs.MenangCode.GDAsapObjects1.length = 0;
gdjs.MenangCode.GDAsapObjects2.length = 0;
gdjs.MenangCode.GDAsapObjects3.length = 0;
gdjs.MenangCode.GDTandaStartObjects1.length = 0;
gdjs.MenangCode.GDTandaStartObjects2.length = 0;
gdjs.MenangCode.GDTandaStartObjects3.length = 0;
gdjs.MenangCode.GDPanelPetaObjects1.length = 0;
gdjs.MenangCode.GDPanelPetaObjects2.length = 0;
gdjs.MenangCode.GDPanelPetaObjects3.length = 0;
gdjs.MenangCode.GDPetaSelObjects1.length = 0;
gdjs.MenangCode.GDPetaSelObjects2.length = 0;
gdjs.MenangCode.GDPetaSelObjects3.length = 0;
gdjs.MenangCode.GDPetaTelurObjects1.length = 0;
gdjs.MenangCode.GDPetaTelurObjects2.length = 0;
gdjs.MenangCode.GDPetaTelurObjects3.length = 0;
gdjs.MenangCode.GDPetaPemainObjects1.length = 0;
gdjs.MenangCode.GDPetaPemainObjects2.length = 0;
gdjs.MenangCode.GDPetaPemainObjects3.length = 0;
gdjs.MenangCode.GDPetaStartObjects1.length = 0;
gdjs.MenangCode.GDPetaStartObjects2.length = 0;
gdjs.MenangCode.GDPetaStartObjects3.length = 0;
gdjs.MenangCode.GDPetaFinishObjects1.length = 0;
gdjs.MenangCode.GDPetaFinishObjects2.length = 0;
gdjs.MenangCode.GDPetaFinishObjects3.length = 0;
gdjs.MenangCode.GDTandaFinishObjects1.length = 0;
gdjs.MenangCode.GDTandaFinishObjects2.length = 0;
gdjs.MenangCode.GDTandaFinishObjects3.length = 0;
gdjs.MenangCode.GDPanahObjects1.length = 0;
gdjs.MenangCode.GDPanahObjects2.length = 0;
gdjs.MenangCode.GDPanahObjects3.length = 0;
gdjs.MenangCode.GDBonekaObjects1.length = 0;
gdjs.MenangCode.GDBonekaObjects2.length = 0;
gdjs.MenangCode.GDBonekaObjects3.length = 0;

gdjs.MenangCode.eventsList2(runtimeScene);
gdjs.MenangCode.GDTeksHebatObjects1.length = 0;
gdjs.MenangCode.GDTeksHebatObjects2.length = 0;
gdjs.MenangCode.GDTeksHebatObjects3.length = 0;
gdjs.MenangCode.GDTeksMenangObjects1.length = 0;
gdjs.MenangCode.GDTeksMenangObjects2.length = 0;
gdjs.MenangCode.GDTeksMenangObjects3.length = 0;
gdjs.MenangCode.GDTeksJumlahBonekaObjects1.length = 0;
gdjs.MenangCode.GDTeksJumlahBonekaObjects2.length = 0;
gdjs.MenangCode.GDTeksJumlahBonekaObjects3.length = 0;
gdjs.MenangCode.GDTombolLagiObjects1.length = 0;
gdjs.MenangCode.GDTombolLagiObjects2.length = 0;
gdjs.MenangCode.GDTombolLagiObjects3.length = 0;
gdjs.MenangCode.GDTombolRakObjects1.length = 0;
gdjs.MenangCode.GDTombolRakObjects2.length = 0;
gdjs.MenangCode.GDTombolRakObjects3.length = 0;
gdjs.MenangCode.GDPetualangObjects1.length = 0;
gdjs.MenangCode.GDPetualangObjects2.length = 0;
gdjs.MenangCode.GDPetualangObjects3.length = 0;
gdjs.MenangCode.GDKepalaPetualangObjects1.length = 0;
gdjs.MenangCode.GDKepalaPetualangObjects2.length = 0;
gdjs.MenangCode.GDKepalaPetualangObjects3.length = 0;
gdjs.MenangCode.GDKelinciObjects1.length = 0;
gdjs.MenangCode.GDKelinciObjects2.length = 0;
gdjs.MenangCode.GDKelinciObjects3.length = 0;
gdjs.MenangCode.GDKepalaKelinciObjects1.length = 0;
gdjs.MenangCode.GDKepalaKelinciObjects2.length = 0;
gdjs.MenangCode.GDKepalaKelinciObjects3.length = 0;
gdjs.MenangCode.GDTelurObjects1.length = 0;
gdjs.MenangCode.GDTelurObjects2.length = 0;
gdjs.MenangCode.GDTelurObjects3.length = 0;
gdjs.MenangCode.GDTelurTerbangObjects1.length = 0;
gdjs.MenangCode.GDTelurTerbangObjects2.length = 0;
gdjs.MenangCode.GDTelurTerbangObjects3.length = 0;
gdjs.MenangCode.GDKeranjangObjects1.length = 0;
gdjs.MenangCode.GDKeranjangObjects2.length = 0;
gdjs.MenangCode.GDKeranjangObjects3.length = 0;
gdjs.MenangCode.GDRumputObjects1.length = 0;
gdjs.MenangCode.GDRumputObjects2.length = 0;
gdjs.MenangCode.GDRumputObjects3.length = 0;
gdjs.MenangCode.GDPohonObjects1.length = 0;
gdjs.MenangCode.GDPohonObjects2.length = 0;
gdjs.MenangCode.GDPohonObjects3.length = 0;
gdjs.MenangCode.GDSemakObjects1.length = 0;
gdjs.MenangCode.GDSemakObjects2.length = 0;
gdjs.MenangCode.GDSemakObjects3.length = 0;
gdjs.MenangCode.GDBungaObjects1.length = 0;
gdjs.MenangCode.GDBungaObjects2.length = 0;
gdjs.MenangCode.GDBungaObjects3.length = 0;
gdjs.MenangCode.GDBatuObjects1.length = 0;
gdjs.MenangCode.GDBatuObjects2.length = 0;
gdjs.MenangCode.GDBatuObjects3.length = 0;
gdjs.MenangCode.GDAsapObjects1.length = 0;
gdjs.MenangCode.GDAsapObjects2.length = 0;
gdjs.MenangCode.GDAsapObjects3.length = 0;
gdjs.MenangCode.GDTandaStartObjects1.length = 0;
gdjs.MenangCode.GDTandaStartObjects2.length = 0;
gdjs.MenangCode.GDTandaStartObjects3.length = 0;
gdjs.MenangCode.GDPanelPetaObjects1.length = 0;
gdjs.MenangCode.GDPanelPetaObjects2.length = 0;
gdjs.MenangCode.GDPanelPetaObjects3.length = 0;
gdjs.MenangCode.GDPetaSelObjects1.length = 0;
gdjs.MenangCode.GDPetaSelObjects2.length = 0;
gdjs.MenangCode.GDPetaSelObjects3.length = 0;
gdjs.MenangCode.GDPetaTelurObjects1.length = 0;
gdjs.MenangCode.GDPetaTelurObjects2.length = 0;
gdjs.MenangCode.GDPetaTelurObjects3.length = 0;
gdjs.MenangCode.GDPetaPemainObjects1.length = 0;
gdjs.MenangCode.GDPetaPemainObjects2.length = 0;
gdjs.MenangCode.GDPetaPemainObjects3.length = 0;
gdjs.MenangCode.GDPetaStartObjects1.length = 0;
gdjs.MenangCode.GDPetaStartObjects2.length = 0;
gdjs.MenangCode.GDPetaStartObjects3.length = 0;
gdjs.MenangCode.GDPetaFinishObjects1.length = 0;
gdjs.MenangCode.GDPetaFinishObjects2.length = 0;
gdjs.MenangCode.GDPetaFinishObjects3.length = 0;
gdjs.MenangCode.GDTandaFinishObjects1.length = 0;
gdjs.MenangCode.GDTandaFinishObjects2.length = 0;
gdjs.MenangCode.GDTandaFinishObjects3.length = 0;
gdjs.MenangCode.GDPanahObjects1.length = 0;
gdjs.MenangCode.GDPanahObjects2.length = 0;
gdjs.MenangCode.GDPanahObjects3.length = 0;
gdjs.MenangCode.GDBonekaObjects1.length = 0;
gdjs.MenangCode.GDBonekaObjects2.length = 0;
gdjs.MenangCode.GDBonekaObjects3.length = 0;


return;

}

gdjs['MenangCode'] = gdjs.MenangCode;
