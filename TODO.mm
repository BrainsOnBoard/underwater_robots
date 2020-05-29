<map version="freeplane 1.8.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="TODO" FOLDED="false" ID="ID_1522354215" CREATED="1590752883575" MODIFIED="1590752891895" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="6" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Do auto-RIDF for &quot;proper&quot; panoramic image, using ~53° slice, to see what we would expect in ideal case" POSITION="right" ID="ID_1263276957" CREATED="1590752891912" MODIFIED="1590752943424">
<edge COLOR="#ff0000"/>
</node>
<node TEXT="Figure out why single-image RIDF not working even for easy case (e.g. images1)" POSITION="right" ID="ID_932931406" CREATED="1590752944220" MODIFIED="1590752962504">
<edge COLOR="#0000ff"/>
<node TEXT="Try preprocessing" ID="ID_490781779" CREATED="1590752994805" MODIFIED="1590753001758">
<node TEXT="Histeq" ID="ID_1343883740" CREATED="1590753001762" MODIFIED="1590753004399"/>
<node TEXT="Downsampling" ID="ID_907356923" CREATED="1590753004796" MODIFIED="1590753007367"/>
</node>
</node>
<node TEXT="Try better stitching: overlap + interp" POSITION="right" ID="ID_69685330" CREATED="1590752963964" MODIFIED="1590752985935">
<edge COLOR="#00ff00"/>
</node>
<node TEXT="Look at single column of pixels which is &quot;shared&quot; between images" POSITION="right" ID="ID_695732639" CREATED="1590753016293" MODIFIED="1590753039872">
<edge COLOR="#00ffff"/>
</node>
<node TEXT="Feature tracking" POSITION="right" ID="ID_1720672399" CREATED="1590753040541" MODIFIED="1590753048735">
<edge COLOR="#7c0000"/>
<node TEXT="Vertical feature" ID="ID_454888708" CREATED="1590753049189" MODIFIED="1590753067873"/>
<node TEXT="Horizontal feature" ID="ID_288948562" CREATED="1590753061037" MODIFIED="1590753072135"/>
<node TEXT="(Use e.g. edges of tiles in empty bath image set)" ID="ID_894223809" CREATED="1590753072645" MODIFIED="1590753097417"/>
</node>
</node>
</map>
