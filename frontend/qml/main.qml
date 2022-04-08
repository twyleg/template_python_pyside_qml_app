import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

import "./items"

Window {
	width: 640
	height: 480
	visible: true
	title: qsTr("Stopwatch")

	color: "black"

	Item {
		id: dialItem

		width: parent.width
		height: parent.height * 0.8

		anchors.horizontalCenter: parent
		anchors.top: parent.top

		Dial {
			anchors.centerIn: parent

			diameter: Math.min(parent.width, parent.height)
		}

	}

	Item {
		id: controlItem

		anchors.top: dialItem.bottom
		anchors.bottom: parent.bottom
		anchors.left: dialItem.left
		anchors.right: dialItem.right

		anchors.topMargin: 5
		anchors.bottomMargin: 5

		Button {

			anchors.fill: parent

			text: "Millis: " + time.millis
		}
	}

}
