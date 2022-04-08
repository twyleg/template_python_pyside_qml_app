import QtQuick 2.0

Rectangle {

	property int diameter

	radius: diameter / 2
	width: diameter
	height: diameter

	color: "white"

	border.color: "black"
	border.width: 5

}
