package org.continuumxr.shell

import android.app.Activity
import android.os.Build
import android.os.Bundle
import android.widget.TextView

class CxrShellActivity : Activity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)

    val cxrVersion = getSystemProperty("ro.cxr.version") ?: "unknown"
    val buildPhase = getSystemProperty("ro.cxr.build_phase") ?: "unknown"

    findViewById<TextView>(R.id.version).text = "v$cxrVersion — Phase $buildPhase"

    findViewById<TextView>(R.id.device_info).text = buildString {
      appendLine("Model: ${Build.MODEL}")
      appendLine("Device: ${Build.DEVICE}")
      appendLine("Brand: ${Build.BRAND}")
      appendLine("Android: ${Build.VERSION.RELEASE} (API ${Build.VERSION.SDK_INT})")
      appendLine("CXR Version: $cxrVersion")
      append("Build Phase: $buildPhase")
    }
  }

  override fun onBackPressed() {
    // Do nothing — this is the home screen
  }

  private fun getSystemProperty(key: String): String? {
    return try {
      val clazz = Class.forName("android.os.SystemProperties")
      val method = clazz.getMethod("get", String::class.java)
      val value = method.invoke(null, key) as String
      value.ifEmpty { null }
    } catch (e: Exception) {
      null
    }
  }
}
